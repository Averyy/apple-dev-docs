# count

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The number of feature providers in this batch.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var count: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger count;
```

## See Also

### Accessing values
- [func features(at: Int) -> any MLFeatureProvider](./features%28at%29.md)
  Returns the feature provider at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlbatchprovider/count)*