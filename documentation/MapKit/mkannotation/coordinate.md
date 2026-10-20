# coordinate

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The center point (specified as a map coordinate) of the annotation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var coordinate: CLLocationCoordinate2D { get }
```

```objc
@property (nonatomic, readonly) CLLocationCoordinate2D coordinate;
```

#### Discussion

Your implementation of this property must be key-value observing (KVO) compliant. For more information on how to implement support for KVO, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotation/coordinate)*