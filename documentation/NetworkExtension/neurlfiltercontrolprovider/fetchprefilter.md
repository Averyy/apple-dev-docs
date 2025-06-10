# fetchPrefilter()

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

Fetches pre-filter data, in response to a call from the framework.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func fetchPrefilter() async throws -> NEURLFilterPrefilter?
```

#### Return Value

An [`NEURLFilterPrefilter`](neurlfilterprefilter.md) that contains the prefilter information. The initial fetch must return a valid [`NEURLFilterPrefilter`](neurlfilterprefilter.md). Returning a `nil` prefilter for subsequent fetch indicates no change; in this case, the system continues to use the current prefilter data.

#### Discussion

The system calls this method at the frequency specified by [`prefilterFetchInterval`](neurlfiltermanager/prefilterfetchinterval.md). Your implementation overrides this method to perform whatever steps are necessary to fetch pre-filter data. Make sure the first call to this method returns a non-`nil` Bloom filter. On subsequent calls, you can return `nil` to indicate no change to the current Bloom filter. In this case, the system continues to use the previously-provided Bloom filter.

The fetched pre-filter data must be a Bloom filter using the 32-bit FNV-1a and 32-bit MurmurHash3 hash functions, with double hashing. Both the FNV-1a and MurmurHash3 hash functions are fast non-cryptographic hash functions that produce good distribution. Adding double hashing further improves the spread and distribution of hash values over a Bloom filter’s bit array.

Note that the [`bitCount`](neurlfilterprefilter/bitcount.md) and [`hashCount`](neurlfilterprefilter/hashcount.md) are calculated based on number of items in the data set as well as the false-positive tolerance selected for the Bloom filter. The selected false-positive tolerance must be relatively low to allow for accurate and efficient pre-filtering.

Given the number of items in the data set, `n`, select the false-positive tolerance, `p`, in the range between `0.0` and `1.0`, excluding the bounds:

Composition of the Bloom filter as well as membership testing must deploy the same indexing operations, where `x` is the data string to be inserted or checked:

```not specified
h1(x) = FNV-1a(x)
h2(x) = MurmurHash3(x) with murmurSeed

for each index i in the range from 0 to < hashCount
	hashes[i] = (h1(x) + i * h2(x)) mod bitCount
```

For composition, set the bits to `1` at each of the positions in `hashes[]`. For membership testing, verify if all the bits at positions in `hashes[]` are `1`.

Your provider implementation can return the complete Bloom filter data if the Bloom filter data is relatively small. Otherwise, the implementation can save the Bloom filter data in a temporary file and return the file path.

## See Also

- [struct NEURLFilterPrefilter](neurlfilterprefilter.md)
  A structure containing a prefilter returned by a filter control provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolprovider/fetchprefilter())*