# typeID

**Framework**: Core Graphics  
**Kind**: property

Returns the unique type identifier used for [`CGLayer`](cglayer.md) objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var typeID: CFTypeID { get }
```

#### Discussion

A type identifier is an integer that identifies the opaque type to which a Core Foundation object belongs. You use type IDs in various contexts, such as when you are operating on heterogeneous collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglayer/typeid)*