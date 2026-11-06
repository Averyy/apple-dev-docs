# DynamicInstructionsGroup

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A dynamic instructions type that groups its content so a single modifier can apply to the whole group.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
struct DynamicInstructionsGroup<Content> where Content : DynamicInstructions
```

## Overview

Use `Group` to gather several instructions and tools under one lifecycle, for example to run a single `onActivate` / `onDeactivate` for the entire group:

```swift
struct MyInstructions: DynamicInstructions {
  var body: some DynamicInstructions {
    Group {
      Instructions("You are a helpful assistant.")
      SomeTool()
    }
    .onActivate {
      activeInstructions = "assistant"
    }
  }
}
```

## Topics

### Initializers
- [init(content: () -> Content)](./dynamicinstructionsgroup/init%28content%29.md)
  Creates a group from the content you specify.

## Relationships

### Conforms To
- [DynamicInstructions](./dynamicinstructions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructionsgroup)*