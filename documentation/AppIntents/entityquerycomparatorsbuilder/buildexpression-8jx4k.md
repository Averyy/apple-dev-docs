# buildExpression(_:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func buildExpression<InputType>(_ expression: IsBetweenComparator<Property, PropertyType, InputType, ComparatorMappingType>) -> AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType> where InputType : Comparable, InputType == PropertyType.UnwrappedType
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerycomparatorsbuilder/buildexpression(_:)-8jx4k)*