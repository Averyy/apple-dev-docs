# maximumNumberOfResultsPerPage

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The maximum number of results to return in a single page enumeration.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var maximumNumberOfResultsPerPage: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger maximumNumberOfResultsPerPage;
```

#### Discussion

If the extension returns more than this number of results in a single page enumeration, the system will crash the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchenumerationobserver/maximumnumberofresultsperpage)*