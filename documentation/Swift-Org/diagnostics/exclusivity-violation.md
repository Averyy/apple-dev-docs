---
url: "https://docs.swift.org/latest/documentation/diagnostics/exclusivity-violation"
framework: "Swift-Org/diagnostics"
---

# Overlapping accesses, but operation requires exclusive access (ExclusivityViolation)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

Swift requires exclusive access to a variable in order to modify that variable. An error is reported if a program attempts to access a variable while it is already in the process of being accessed via another name. These issues can often be resolved by making a local copy of a variable before modifying it.

In the following example, `count` is accessed for modification by passing it as an `inout` argument to `modifyTwice`. This `inout` access to `count` lasts for the entire duration of the `modifyTwice` function call. The exclusivity violation occurs because the `modifier` closure also accesses `count` via the name `$0` while the first access is in progress.

```swift
func modifyTwice(_ value: inout Int, by modifier: (inout Int) -> ()) {
  modifier(&value)
  modifier(&value)
}

func testCount() {
  var count = 1
  modifyTwice(&count) { $0 += count } // error: overlapping accesses to 'count', but modification requires exclusive access; consider copying to a local variable
  print(count)
}
```

This exclusivity violation can be fixed by introducing a local variable to track the value the `modifier` closure should add to its argument.

```swift
func modifyTwice(_ value: inout Int, by modifier: (inout Int) -> ()) {
  modifier(&value)
  modifier(&value)
}

func testCount() {
  var count = 1
  let incrementBy = count
  modifyTwice(&count) { $0 += incrementBy }
  print(count)
}
```

In this updated program, `count` and `$0` no longer refer to the same variable, so accessing them at the same time does not violate exclusivity.

Another common source of exclusivity violations occurs when a `mutating` method modifies `self`:

```swift
extension Array {
    mutating func append(removingFrom other: inout Array<Element>) {
        while !other.isEmpty {
            self.append(other.removeLast())
        }
    }
}

var numbers = [1, 2, 3]
numbers.append(removingFrom: &numbers) // error: overlapping accesses to 'x', but modification requires exclusive access; consider copying to a local variable
```

A `mutating` method accesses `self` for the duration of the method call, so in this example `numbers` has two conflicting long-lived accesses, one as `self` and one as an `inout` argument to the method. Again, a local variable can be introduced to eliminate the conflict:

```swift
var numbers = [1, 2, 3]
var toAppend = numbers
numbers.append(removingFrom: &toAppend)
```

Exclusivity checks play an important role in enforcing memory safety and enabling compiler optimizations. See the Swift.org [Swift 5 exclusivity enforcement](https://www.swift.org/blog/swift-5-exclusivity/) to learn more.

## See Also

### Related Documentation
- [Swift 5 exclusivity enforcement](https://www.swift.org/blog/swift-5-exclusivity/)
- [@dynamicCallable implementation requirements (DynamicCallable)](./dynamic-callable-requirements.md)
- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
- [Always enabled availability domains (AlwaysAvailableDomain)](./always-available-domain.md)
  Warnings that identify `@available` attributes and `if #available` statements that reference custom availability domains which have been permanently enabled.
- [Argument matching for trailing closures (TrailingClosureMatching)](./trailing-closure-matching.md)
- [Calling a mutating async actor-isolated method (ActorIsolatedMutatingAsync)](./actor-isolated-mutating-async.md)
- [Calling an actor-isolated method from a synchronous nonisolated context (ActorIsolatedCall)](./actor-isolated-call.md)
- [Captures in a `@Sendable` closure (SendableClosureCaptures)](./sendable-closure-captures.md)
- [Compilation caching (CompilationCaching)](./compilation-caching.md)
  Errors and warnings related to the compiler’s CAS compilation caching.
- [Conforming to `StringInterpolationProtocol` (StringInterpolationConformance)](./string-interpolation-conformance.md)
- [Conversion from `@isolated(any)` function type to synchronous function type (ConversionFromIsolatedAnyToSynchronous)](./conversion-from-isolated-any-to-synchronous.md)
- [Deprecated declaration warnings (DeprecatedDeclaration)](./deprecated-declaration.md)
  Warnings related to deprecated APIs that may be removed in future versions and should be replaced with more current alternatives.
- [Deprecated implementation-only imports (ImplementationOnlyDeprecated)](./implementation-only-deprecated.md)
  Warnings that identify `import` declarations with the `@_implementationOnly` attribute.
- [Dynamic exclusivity (DynamicExclusivity)](./dynamic-exclusivity.md)
  Experimental
- [Embedded Swift language restrictions (EmbeddedRestrictions)](./embedded-restrictions.md)
  Embedded Swift is a subset of the Swift language that that introduces some restrictions on the use of language features to eliminate the need for the Swift runtime. These restrictions are captured by the `EmbeddedRestrictions` diagnostic group.
- [Existential Types and Performance (ExistentialType)](./existential-type.md)


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/exclusivity-violation)*