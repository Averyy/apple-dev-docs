# fetchPrefilter(existingPrefilterTag:)

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

Fetches prefilter data, in response to a call from the framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func fetchPrefilter(existingPrefilterTag: String?) async throws -> NEURLFilterPrefilter?
```

#### Return Value

An [`NEURLFilterPrefilter`](neurlfilterprefilter.md) that contains the prefilter information. The initial fetch must return a valid [`NEURLFilterPrefilter`](neurlfilterprefilter.md). Returning a `nil` prefilter for subsequent fetches indicates no change; in this case, the system continues to use the current prefilter data.

#### Discussion

The system calls this method at the frequency specified by [`prefilterFetchInterval`](neurlfiltermanager/prefilterfetchinterval.md). Your implementation overrides this method to perform whatever steps are necessary to fetch prefilter data. Make sure the first call to this method returns a non-`nil` Bloom filter. On subsequent calls, you can return `nil` to indicate no change to the current Bloom filter. In this case, the system continues to use the previously provided Bloom filter.

The fetched prefilter data must be a Bloom filter using the 32-bit FNV-1a and 32-bit MurmurHash3 hash functions, with double hashing. Both the FNV-1a and MurmurHash3 hash functions are fast noncryptographic hash functions that produce good distribution. Adding double hashing further improves the spread and distribution of hash values over a Bloom filter’s bit array.

Note that the [`bitCount`](neurlfilterprefilter/bitcount.md) and [`hashCount`](neurlfilterprefilter/hashcount.md) are calculated based on number of items in the data set as well as the false-positive tolerance selected for the Bloom filter. The selected false-positive tolerance must be relatively low to allow for accurate and efficient prefiltering.

Given the number of items in the data set, `n`, select the false-positive tolerance, `p`, in the range between `0.0` and `1.0`, excluding the bounds, you can calculate the [`bitCount`](neurlfilterprefilter/bitcount.md) and [`hashCount`](neurlfilterprefilter/hashcount.md) as follows:

| Variable | Meaning | Calculation |
| --- | --- | --- |
| `bitCount` | The number of bits in the Bloom filter. | `bitCount = -n * ln(p) / (ln(2) ^ 2)` |
| `hashCount` | The number of hashes in the Bloom filter. | `hashCount = (bitCount / n) * ln(2)` |

Composition of the Bloom filter as well as membership testing must deploy the same indexing operations, where `x` is the data string to be insert or check:

```not specified
h1(x) = FNV-1a(x)
h2(x) = MurmurHash3(x) with murmurSeed

for each index i in the range from 0 to < hashCount
    hashes[i] = (h1(x) + i * h2(x)) mod bitCount
```

For composition, set the bits to `1` at each of the positions in `hashes[]`. For membership testing, verify if all the bits at positions in `hashes[]` are `1`.

The input data set contains the URLs you want to block. All URLs in the data set must already be puny-coded before constructing the Bloom filter.

Your provider implementation can return the complete Bloom filter data if the Bloom filter data is relatively small. Otherwise, the implementation can save the Bloom filter data in a temporary file and return the file path.

> **Note**: An optional error to indicate the failure reason.

## Parameters

- `existingPrefilterTag`: The tag of the current Bloom filter.  The system passes the tag of the last fetched Bloom filter, or   for the initial fetch. Your implementation can use this tag to decide if a Bloom filter update is necessary.  If an update isn’t necessary, return   to tell the system to continue using the current Bloom filter.

## See Also

- [struct NEURLFilterPrefilter](neurlfilterprefilter.md)
  A structure containing a prefilter returned by a filter control provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolprovider/fetchprefilter(existingprefiltertag:))*