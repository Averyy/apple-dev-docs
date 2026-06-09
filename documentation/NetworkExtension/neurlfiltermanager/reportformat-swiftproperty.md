# reportFormat

**Framework**: Network Extension  
**Kind**: property

The format the manager uses to send blocked URL reports.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
var reportFormat: NEURLFilterManager.ReportFormat { get set }
```

#### Discussion

Use the values in the [`NEURLFilterManager.ReportFormat`](neurlfiltermanager/reportformat-swift.enum.md) enumeration to specify the format to use. By default, the manager uses the [`NEURLFilterManager.ReportFormat.json`](neurlfiltermanager/reportformat-swift.enum/json.md) format.

##### Handling Json Results

When you specify the [`NEURLFilterManager.ReportFormat.json`](neurlfiltermanager/reportformat-swift.enum/json.md) format, your endpoint receives data in JSON as a simple array of strings. The structure of this data is like the following:

```json
[
	"example.com",
	"example2.com",
	"example3.com"
]
```

##### Handling Protobuf Results

When you specify the [`NEURLFilterManager.ReportFormat.protobuf`](neurlfiltermanager/reportformat-swift.enum/protobuf.md) format, your endpoint receives the Protocol Buffers wire format with manual encoding for a repeated string field. Each URL entry follows this binary structure:

- **Field Tag**: 1 byte (`0x0A` = field number 1, wire type 2 for length-delimited).
- **String Length**: A variable-length integer (varint) encoding the byte length of the URL string.
- **String Data**: UTF-8 encoded URL bytes.

For strings under 128 bytes, the length is a single byte. For longer strings, the protocol uses varint encoding, where each byte has the MSB set (`0x80`) except the final byte.

The following example shows the encoding of the URL `https://example.com`:

```not specified
Example encoding for URL "https://example.com":
[0x0A]    [0x13]    [h][t][t][p][s][:][/][/][e][x][a][m][p][l][e][.][c][o][m]
^tag      ^len=19   ^------------ 19 bytes of UTF-8 string data ------------^
```

## See Also

- [var reportEndpoint: String?](neurlfiltermanager/reportendpoint.md)
  The endpoint that the filter manager sends blocked URL reports to.
- [NEURLFilterManager.ReportFormat](neurlfiltermanager/reportformat-swift.enum.md)
  An enumertion of report format types used when reporting blocked URLs.
- [var reportInterval: TimeInterval](neurlfiltermanager/reportinterval.md)
  The time interval (in seconds) at which the system sends reports of blocked URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/reportformat-swift.property)*