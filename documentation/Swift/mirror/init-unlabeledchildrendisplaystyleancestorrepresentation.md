# init(_:unlabeledChildren:displayStyle:ancestorRepresentation:)

**Framework**: Swift  
**Kind**: init

Creates a mirror representing the given subject with unlabeled children.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init<Subject, C>(_ subject: Subject, unlabeledChildren: C, displayStyle: Mirror.DisplayStyle? = nil, ancestorRepresentation: Mirror.AncestorRepresentation = .generated) where C : Collection
```

#### Discussion

You use this initializer from within your type’s `customMirror` implementation to create a customized mirror, particularly for custom types that are collections. The labels of the resulting mirror’s `children` collection are all `nil`.

If `subject` is a class instance, `ancestorRepresentation` determines whether ancestor classes will be represented and whether their `customMirror` implementations will be used. By default, the `customMirror` implementation of any ancestors is ignored. To prevent bypassing customized ancestors, pass `.customized({ super.customMirror })` as the `ancestorRepresentation` parameter when implementing your type’s `customMirror` property.

## Parameters

- `subject`: The instance to represent in the new mirror.
- `unlabeledChildren`: The children to use for the mirror. The collection   traversal modeled by   is captured so that the   resulting mirror’s children may be upgraded to a bidirectional or   random access collection later. See the   property for   details.
- `displayStyle`: The preferred display style for the mirror when   presented in the debugger or in a playground. The default is  .
- `ancestorRepresentation`: The means of generating the subject’s   ancestor representation.   is ignored if    is not a class instance. The default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirror/init(_:unlabeledchildren:displaystyle:ancestorrepresentation:))*