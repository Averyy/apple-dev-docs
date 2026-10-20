# buildLimitedAvailability(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any Commands) -> some Commands
```

**Other overloads**:

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any CustomizableToolbarContent) -> some CustomizableToolbarContent
```

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any SceneAccessoryContent) -> some SceneAccessoryContent
```

```swift
@export(implementation)
static func buildLimitedAvailability(_ content: any ToolbarContent) -> some ToolbarContent
```

```swift
@export(implementation)
static func buildLimitedAvailability<Content>(_ content: Content) -> AnyView where Content : View
```

```swift
static func buildLimitedAvailability(_ content: some ChartContent) -> AnyChartContent
```

## See Also

### Conditionally building content
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](./buildeither%28first%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](./buildeither%28second%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static buildIf(_:)](./buildif%28_%29.md)
  Produces optional content for conditional statements in multi-statement closures that’s only included when the condition evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewbuilder/buildlimitedavailability(_:))*