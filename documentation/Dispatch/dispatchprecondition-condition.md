# dispatchPrecondition(condition:)

**Framework**: Dispatch  
**Kind**: func

Checks a dispatch condition necessary for further execution.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)
```

#### Discussion

Use this function to detect conditions about the current execution context that must prevent the program from proceeding even in shipping code.

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration): if `condition` evaluates to `false`, stop program execution in a debuggable state.
- In `-O` builds (the default for Xcode’s Release configuration): if `condition` evaluates to `false`, stop program execution.
- In `-Ounchecked` builds, `condition` is not evaluated, but the optimizer may assume that it would evaluate to `true`. Failure to satisfy that assumption in `-Ounchecked` builds is a serious programming error.

## Parameters

- `condition`: A dispatch predicate for the current context to check.

## See Also

- [class DispatchObject](dispatchobject.md)
  The base class for most dispatch types.
- [enum DispatchPredicate](dispatchpredicate.md)
  Logical conditions to evaluate within a given execution context.
- [Dispatch Objects](dispatch-objects.md)
  The basic behaviors supported by all dispatch types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchprecondition(condition:))*