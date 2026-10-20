# CommandsBuilder

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Constructs command sets from multi-expression closures. Like `ContentBuilder`, it supports up to ten expressions in the closure body.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@resultBuilder
struct CommandsBuilder
```

## Topics

### Building content
- [static func buildBlock() -> EmptyCommands](./commandsbuilder/buildblock%28%29.md)
  Builds an empty command set from a block containing no statements.
- [static func buildBlock<C>(C) -> C](./commandsbuilder/buildblock%28_%29.md)
  Passes a single command group written as a child group through modified.
- [static func buildBlock<C0, C1>(C0, C1) -> some Commands](./commandsbuilder/buildblock%28_,_%29.md)
- [static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some Commands](./commandsbuilder/buildblock%28_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some Commands](./commandsbuilder/buildblock%28_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some Commands](./commandsbuilder/buildblock%28_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) -> some Commands](./commandsbuilder/buildblock%28_,_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5, C6) -> some Commands](./commandsbuilder/buildblock%28_,_,_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4, C5, C6, C7) -> some Commands](./commandsbuilder/buildblock%28_,_,_,_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3, C4, C5, C6, C7, C8) -> some Commands](./commandsbuilder/buildblock%28_,_,_,_,_,_,_,_,_%29.md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9) -> some Commands](./commandsbuilder/buildblock%28_,_,_,_,_,_,_,_,_,_%29.md)
### Building conditionally
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](./commandsbuilder/buildeither%28first%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](./commandsbuilder/buildeither%28second%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildIf<C>(C?) -> C?](./commandsbuilder/buildif%28_%29.md)
  Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [static func buildLimitedAvailability(any Commands) -> some Commands](./commandsbuilder/buildlimitedavailability%28_%29.md)
  Processes commands for a conditional compiler-control statement that performs an availability check.
- [static func buildExpression<Content>(Content) -> Content](./commandsbuilder/buildexpression%28_%29.md)
  Builds an expression within the builder.

## See Also

### Defining commands
- [func commands<Content>(content: () -> Content) -> some Scene](./scene/commands%28content%29.md)
  Adds commands to the scene.
- [func commandsRemoved() -> some Scene](./scene/commandsremoved%28%29.md)
  Removes all commands defined by the modified scene.
- [func commandsReplaced<Content>(content: () -> Content) -> some Scene](./scene/commandsreplaced%28content%29.md)
  Replaces all commands defined by the modified scene with the commands from the builder.
- [protocol Commands](./commands.md)
  Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [struct CommandMenu](./commandmenu.md)
  Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [struct CommandGroup](./commandgroup.md)
  Groups of controls that you can add to existing command menus.
- [struct CommandGroupPlacement](./commandgroupplacement.md)
  The standard locations that you can place new command groups relative to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandsbuilder)*