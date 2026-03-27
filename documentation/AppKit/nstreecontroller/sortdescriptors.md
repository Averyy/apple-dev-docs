# sortDescriptors

**Framework**: AppKit  
**Kind**: property

An array containing the sort descriptors used to arrange the tree controller’s content.

**Availability**:
- macOS ?+

## Declaration

```swift
var sortDescriptors: [NSSortDescriptor] { get set }
```

#### Discussion

When the value of this property is an empty array, the tree controller has no sort descriptors configured, which means that the contents are arranged in their natural order. This property is observable using key-value observing.

## See Also

- [Cocoa Bindings](cocoa-bindings.md)
  Automatically synchronize your data model with your app’s interface using Cocoa Bindings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/sortdescriptors)*