# IntentChoiceOption.Style

**Framework**: App Intents  
**Kind**: struct

Defines the visual style and semantic meaning of an [`IntentChoiceOption`](intentchoiceoption.md).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Style
```

#### Overview

The system uses the style to render the option appropriately in the user interface.

## Topics

### Operators
- [static func == (IntentChoiceOption.Style, IntentChoiceOption.Style) -> Bool](intentchoiceoption/style-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intentchoiceoption/style-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentchoiceoption/style-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var cancel: IntentChoiceOption.Style](intentchoiceoption/style-swift.struct/cancel.md)
  Apply a style that indicates the option cancels the operation and leaves things unchanged.
- [static var `default`: IntentChoiceOption.Style](intentchoiceoption/style-swift.struct/default.md)
  Apply the default style to the option’s button.
- [static var destructive: IntentChoiceOption.Style](intentchoiceoption/style-swift.struct/destructive.md)
  Apply a style that indicates the option might change or delete data.
### Default Implementations
- [Equatable Implementations](intentchoiceoption/style-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentchoiceoption/style-swift.struct)*