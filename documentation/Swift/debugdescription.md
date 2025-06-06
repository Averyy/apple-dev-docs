# DebugDescription()

**Framework**: Swift  
**Kind**: macro

Converts description definitions to a debugger Type Summary.

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
@attached
(member) @attached(memberAttribute) macro DebugDescription()
```

#### Overview

This macro converts compatible description implementations written in Swift to an LLDB format known as a Type Summary. A Type Summary is LLDB’s equivalent to `debugDescription`, with the distinction that it does not execute code inside the debugged process. By avoiding code execution, descriptions can be produced faster, without potential side effects, and shown in situations where code execution is not performed, such as the variable list of an IDE.

Consider this an example. This `Team` struct has a `debugDescription` which summarizes some key details, such as the team’s name. The debugger only computes this string on demand - typically via the `po` command. By applying the `DebugDescription` macro, a matching Type Summary is constructed. This allows the user to show a string like “Rams [11-2]”, without executing `debugDescription`. This improves the usability, performance, and reliability of the debugging experience.

```swift
@DebugDescription
struct Team: CustomDebugStringConvertible {
   var name: String
   var wins, losses: Int

   var debugDescription: String {
       "\(name) [\(wins)-\(losses)]"
   }
}
```

The `DebugDescription` macro supports both `debugDescription`, `description`, as well as a third option: a property named `lldbDescription`. The first two are implemented when conforming to the `CustomDebugStringConvertible` and `CustomStringConvertible` protocols. The additional `lldbDescription` property is useful when both `debugDescription` and `description` are implemented, but don’t meet the requirements of the `DebugDescription` macro. If `lldbDescription` is implemented, `DebugDescription` choose it over `debugDescription` and `description`. Likewise, `debugDescription` is preferred over `description`.

##### Description Requirements

The description implementation has the following requirements:

- The body of the description implementation must a single string expression. String concatenation is not supported, use string interpolation instead.
- String interpolation can reference stored properties only, functions calls and other arbitrary computation are not supported. Of note, conditional logic and computed properties are not supported.
- Overloaded string interpolation cannot be used.

## See Also

- [protocol CustomReflectable](customreflectable.md)
  A type that explicitly supplies its own mirror.
- [protocol CustomLeafReflectable](customleafreflectable.md)
  A type that explicitly supplies its own mirror, but whose descendant classes are not represented in the mirror unless they also override `customMirror`.
- [protocol CustomPlaygroundDisplayConvertible](customplaygrounddisplayconvertible.md)
  A type that supplies a custom description for playground logging.
- [typealias PlaygroundQuickLook](playgroundquicklook.md)
  The sum of types that can be used as a Quick Look representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/debugdescription())*