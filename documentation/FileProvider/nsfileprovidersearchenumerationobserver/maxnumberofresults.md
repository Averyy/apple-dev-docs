# maxNumberOfResults

**Framework**: File Provider  
**Kind**: property  
**Required**: Yes

The maximum number of results to return in a single page enumeration.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
var maxNumberOfResults: Int { get }
```

#### Discussion

> ⚠️ **Warning**: If the extension returns more than this number of results in a single page enumeration, the system terminates the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerationobserver/maxnumberofresults)*