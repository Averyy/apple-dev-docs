# LanguageModelSession.SessionBinding

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A property wrapper type that provides a binding to session state from a parent scope.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@propertyWrapper
struct SessionBinding<Value>
```

## Overview

Use `@SessionBinding` when a child component needs to access state that is owned by a parent. The binding must be provided via an initializer.

Unlike `@SessionState` which owns and initializes its value, `@SessionBinding` receives its value from an external source (typically via `$parentState`).

You can use `@SessionBinding` as a property wrapper:

```swift
@SessionBinding var value: Int
```

Or as a type directly:

```swift
var value: SessionBinding<Int>
```

```swift
// Parent component owns the state
struct BudgetWorkflow: DynamicInstructions {
    @SessionState var budget = 100

    var body: some DynamicInstructions {
      IncrementBudget(value: $budget)
    }
}

// Child component receives binding
struct IncrementBudget: Tool {
    @SessionBinding var value: Int

    init(value: SessionBinding<Int>) {
        self._value = value
    }

    func call(arguments: Args) -> String {
        value += arguments.amount
        return "Budget is now \(value)"
    }
}
```

## Topics

### Instance Properties
- [var projectedValue: LanguageModelSession.SessionBinding<Value>](./sessionbinding/projectedvalue.md)
- [var wrappedValue: Value](./sessionbinding/wrappedvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/sessionbinding)*