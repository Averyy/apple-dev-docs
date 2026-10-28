# Observable()

**Framework**: Observation  
**Kind**: macro  
**Role**: Macro

Defines and implements conformance of the Observable protocol.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@attached(member, names: named(_$observationRegistrar), named(access), named(withMutation), named(shouldNotifyObservers))
@attached(memberAttribute) @attached(extension, conformances: Observable) macro Observable()
```

## Mentions

- [Applying Macros](../Swift/applying-macros.md)

## Overview

This macro adds observation support to a custom type and conforms the type to the [`Observable`](./observable.md) protocol. For example, the following code applies the `Observable` macro to the type `Car` making it observable:

```swift
@Observable 
class Car {
   var name: String = ""
   var needsRepairs: Bool = false

   init(name: String, needsRepairs: Bool = false) {
       self.name = name
       self.needsRepairs = needsRepairs
   }
}
```

## See Also

### Observable conformance
- [protocol Observable](./observable.md)
  A type that emits notifications to observers when underlying data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observable())*