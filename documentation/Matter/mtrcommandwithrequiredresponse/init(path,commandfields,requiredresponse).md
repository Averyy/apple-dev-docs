# init(path:commandFields:requiredResponse:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
init(path: MTRCommandPath, commandFields: [String : Any]?, requiredResponse: [NSNumber : [String : Any]]?)
```

```objc
- (instancetype) initWithPath:(MTRCommandPath *) path commandFields:(NSDictionary<NSString *,id> *) commandFields requiredResponse:(NSDictionary<NSNumber *,NSDictionary<NSString *,id> *> *) requiredResponse;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommandwithrequiredresponse/init(path:commandfields:requiredresponse:))*