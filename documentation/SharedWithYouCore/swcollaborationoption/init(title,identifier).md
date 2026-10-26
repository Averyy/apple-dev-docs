# init(title:identifier:)

**Framework**: SharedWithYouCore  
**Kind**: init  
**Role**: Initializer

Creates and initializes a collaboration option object with a provided title and identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(title: String, identifier: String)
```

```objc
+ (SWCollaborationOption *) optionWithTitle:(NSString *) title identifier:(NSString *) identifier;
```

## Parameters

- `title`: A localized string the system displays as a title.
- `identifier`: A unique identifier.

## See Also

### Creating collaboration options
- [convenience init(title: String, identifier: String, subtitle: String, selected: Bool, requiredOptionsIdentifiers: [String])](./init%28title,identifier,subtitle,selected,requiredoptionsidentifiers%29.md)
  Creates and initializes a collaboration option object with the provided values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoption/init(title:identifier:))*