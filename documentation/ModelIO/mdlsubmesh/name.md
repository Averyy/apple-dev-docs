# name

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

A descriptive name for the submesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

```objc
@property (nonatomic, copy) NSString * name;
```

#### Discussion

This property is not used in rendering, but you can use it to keep track of multiple submeshes for debugging. This property can also be populated with useful descriptive information when importing submesh data from an asset file or other source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmesh/name)*