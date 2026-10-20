# isOptional

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this feature is optional.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var isOptional: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isOptional) BOOL optional;
```

#### Discussion

Optional values can be `nil`, for models that have inputs related to features being present or not.

## See Also

### Inspecting a feature
- [var name: String](./name.md)
  The name of this feature.
- [var type: MLFeatureType](./type.md)
  The type of this feature.
- [enum MLFeatureType](../mlfeaturetype.md)
  The possible types for feature values, input features, and output features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturedescription/isoptional)*