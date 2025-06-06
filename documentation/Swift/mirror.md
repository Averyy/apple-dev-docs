# Mirror

**Framework**: Swift  
**Kind**: struct

A representation of the substructure and display style of an instance of any type.

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
struct Mirror
```

#### Overview

A mirror describes the parts that make up a particular instance, such as the instance’s stored properties, collection or tuple elements, or its active enumeration case. Mirrors also provide a “display style” property that suggests how this mirror might be rendered.

Playgrounds and the debugger use the `Mirror` type to display representations of values of any type. For example, when you pass an instance to the `dump(_:_:_:_:)` function, a mirror is used to render that instance’s runtime contents.

```swift
struct Point {
    let x: Int, y: Int
}

let p = Point(x: 21, y: 30)
print(String(reflecting: p))
// Prints "▿ Point
//           - x: 21
//           - y: 30"
```

To customize the mirror representation of a custom type, add conformance to the `CustomReflectable` protocol.

## Topics

### Querying Descendants
- [func descendant(any MirrorPath, any MirrorPath...) -> Any?](mirror/descendant(_:_:).md)
  Returns a specific descendant of the reflected subject, or `nil` if no such descendant exists.
- [protocol MirrorPath](mirrorpath.md)
  A protocol for legitimate arguments to `Mirror`’s `descendant` method.
### Initializers
- [init<Subject>(Subject, children: KeyValuePairs<String, Any>, displayStyle: Mirror.DisplayStyle?, ancestorRepresentation: Mirror.AncestorRepresentation)](mirror/init(_:children:displaystyle:ancestorrepresentation:)-34d91.md)
  Creates a mirror representing the given subject using a dictionary literal for the structure.
- [init<Subject, C>(Subject, children: C, displayStyle: Mirror.DisplayStyle?, ancestorRepresentation: Mirror.AncestorRepresentation)](mirror/init(_:children:displaystyle:ancestorrepresentation:)-4af97.md)
  Creates a mirror representing the given subject with a specified structure.
- [init<Subject, C>(Subject, unlabeledChildren: C, displayStyle: Mirror.DisplayStyle?, ancestorRepresentation: Mirror.AncestorRepresentation)](mirror/init(_:unlabeledchildren:displaystyle:ancestorrepresentation:).md)
  Creates a mirror representing the given subject with unlabeled children.
- [init(reflecting: Any)](mirror/init(reflecting:).md)
  Creates a mirror that reflects on the given instance.
### Instance Properties
- [let children: Mirror.Children](mirror/children-swift.property.md)
  A collection of `Child` elements describing the structure of the reflected subject.
- [let displayStyle: Mirror.DisplayStyle?](mirror/displaystyle-swift.property.md)
  A suggested display style for the reflected subject.
- [let subjectType: any Any.Type](mirror/subjecttype.md)
  The static type of the subject being reflected.
- [var superclassMirror: Mirror?](mirror/superclassmirror.md)
  A mirror of the subject’s superclass, if one exists.
### Type Aliases
- [typealias Child](mirror/child.md)
  An element of the reflected instance’s structure.
- [typealias Children](mirror/children-swift.typealias.md)
  The type used to represent substructure.
### Enumerations
- [Mirror.AncestorRepresentation](mirror/ancestorrepresentation.md)
  The representation to use for ancestor classes.
- [Mirror.DisplayStyle](mirror/displaystyle-swift.enum.md)
  A suggestion of how a mirror’s subject is to be interpreted.
### Default Implementations
- [CustomReflectable Implementations](mirror/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](mirror/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)

## See Also

- [struct ObjectIdentifier](objectidentifier.md)
  A unique identifier for a class instance or metatype.
- [func type<T, Metatype>(of: T) -> Metatype](type(of:).md)
  Returns the dynamic type of a value.
- [func == ((any Any.Type)?, (any Any.Type)?) -> Bool](==(_:_:)-w1qf.md)
  Returns a Boolean value indicating whether two types are identical.
- [func != ((any Any.Type)?, (any Any.Type)?) -> Bool](!=(_:_:)-6s4z0.md)
  Returns a Boolean value indicating whether two types are not identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mirror)*