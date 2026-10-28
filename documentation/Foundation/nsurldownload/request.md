# request

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the request that initiated the receiver’s download.

**Availability**:
- macOS 10.2+

## Declaration

```swift
var request: URLRequest { get }
```

```objc
@property (copy, readonly) NSURLRequest * request;
```

## Return Value

The URL request that initiated the receiver’s download.

## See Also

### Getting download properties
- [var deletesFileUponFailure: Bool](./deletesfileuponfailure.md)
  Returns whether the receiver deletes partially downloaded files when a download stops prematurely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurldownload/request)*