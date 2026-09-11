# as(_:)

**Framework**: App Intents Testing  
**Kind**: method

Casts the value to the given type.

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
func `as`<IntentType>(_ type: IntentType) throws -> IntentType.Instance where IntentType : AppIntentTypeDefinition
```

#### Discussion

If the value’s type doesn’t match, this method throws an error.

```swift
let CoffeeEntity = definitions.entities["CoffeeEntity"]
let coffee: AnyAppEntity = try result.value.as(CoffeeEntity)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath/as(_:)-6n9rh)*