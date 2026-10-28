# sources

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

An unordered array of objects that represent accounts that contain calendars.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sources: [EKSource] { get }
```

```objc
@property (nonatomic, readonly) NSArray<EKSource *> * sources;
```

## Discussion

Although this property is an array, the order of the elements in the array isn’t guaranteed.

## See Also

### Accessing account sources
- [var delegateSources: [EKSource]](./delegatesources.md)
  The event sources delegated to the person using your app.
- [func source(withIdentifier: String) -> EKSource?](./source%28withidentifier%29.md)
  Locates an event source with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/sources)*