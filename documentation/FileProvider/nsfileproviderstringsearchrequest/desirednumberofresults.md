# desiredNumberOfResults

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

How many results the system is requesting. This is a hint to the extension, to help avoid unnecessary work. The extension may return more results than this.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var desiredNumberOfResults: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger desiredNumberOfResults;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderstringsearchrequest/desirednumberofresults)*