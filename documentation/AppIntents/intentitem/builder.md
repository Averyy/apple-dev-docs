# IntentItem.Builder

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@resultBuilder
enum Builder
```

Available when `Value` conforms to `_IntentValue`.

## Topics

### Type Methods
- [static func buildArray([[IntentItem<Value>]]) -> [IntentItem<Value>]](./builder/buildarray%28_%29.md)
- [static func buildBlock() -> [Value]](./builder/buildblock%28%29.md)
- [static func buildBlock(IntentItem<Value>...) -> [IntentItem<Value>]](./builder/buildblock%28_%29-9j0sn.md)
- [static func buildBlock([IntentItem<Value>]) -> [IntentItem<Value>]](./builder/buildblock%28_%29-pgo1.md)
- [static func buildExpression(Value) -> IntentItem<Value>](./builder/buildexpression%28_%29-202yw.md)
- [static func buildExpression<ExpressionValue>(IntentItem<ExpressionValue>) -> IntentItem<ExpressionValue>](./builder/buildexpression%28_%29-90pb0.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentitem/builder)*