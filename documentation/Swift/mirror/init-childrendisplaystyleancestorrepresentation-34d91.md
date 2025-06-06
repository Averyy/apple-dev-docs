# init(_:children:displayStyle:ancestorRepresentation:)

**Framework**: Swift  
**Kind**: init

Creates a mirror representing the given subject using a dictionary literal for the structure.

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
init<Subject>(_ subject: Subject, children: KeyValuePairs<String, Any>, displayStyle: Mirror.DisplayStyle? = nil, ancestorRepresentation: Mirror.AncestorRepresentation = .generated)
```

#### Discussion

You use this initializer from within your type’s `customMirror` implementation to create a customized mirror. Pass a dictionary literal with string keys as `children`. Although an  dictionary is arbitrarily-ordered, when you create a mirror with a dictionary literal, the ordering of the mirror’s `children` will exactly match that of the literal you pass.

If `subject` is a class instance, `ancestorRepresentation` determines whether ancestor classes will be represented and whether their `customMirror` implementations will be used. By default, the `customMirror` implementation of any ancestors is ignored. To prevent bypassing customized ancestors, pass `.customized({ super.customMirror })` as the `ancestorRepresentation` parameter when implementing your type’s `customMirror` property.

## Parameters

- `subject`: The instance to represent in the new mirror.
- `children`: A dictionary literal to use as the structure for the   mirror. The   collection of the resulting mirror may be   upgraded to a random access collection later. See the    property for details.
- `displayStyle`: The preferred display style for the mirror when   presented in the debugger or in a playground. The default is  .
- `ancestorRepresentation`: The means of generating the subject’s   ancestor representation.   is ignored if    is not a class instance. The default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirror/init(_:children:displaystyle:ancestorrepresentation:)-34d91)*