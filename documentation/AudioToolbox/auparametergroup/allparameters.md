# allParameters

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

Returns a flat array of all parameters in the group, including those in child groups.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allParameters: [AUParameter] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) NSArray<AUParameter *> * allParameters;
```

*macOS*

```objc
@property (atomic, readonly) NSArray<AUParameter *> * allParameters;
```

## See Also

### Obtaining Group Parameters
- [var children: [AUParameterNode]](./children.md)
  The group’s child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/allparameters)*