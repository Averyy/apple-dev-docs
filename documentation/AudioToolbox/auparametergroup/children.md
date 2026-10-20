# children

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The group’s child nodes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var children: [AUParameterNode] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) NSArray<AUParameterNode *> * children;
```

*macOS*

```objc
@property (atomic, readonly) NSArray<AUParameterNode *> * children;
```

## See Also

### Obtaining Group Parameters
- [var allParameters: [AUParameter]](./allparameters.md)
  Returns a flat array of all parameters in the group, including those in child groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametergroup/children)*