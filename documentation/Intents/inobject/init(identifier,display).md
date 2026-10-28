# init(identifier:display:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a custom intent object with the specified identifier and display string.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
convenience init(identifier: String?, display displayString: String)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier displayString:(NSString *) displayString;
```

## Return Value

A new [`INObject`](../inobject.md), or `nil` if the initializer couldn’t create the object.

## Parameters

- `identifier`: A string that identifies the custom object within your app.
- `displayString`: A string that Siri displays that describes the parameter or property.

## See Also

### Creating a Custom Object
- [convenience init(identifier: String?, display: String, subtitle: String?, image: INImage?)](./init%28identifier,display,subtitle,image%29.md)
  Creates a custom intent object with full display information.
- [convenience init(identifier: String?, display: String, pronunciationHint: String?, subtitle: String?, image: INImage?)](./init%28identifier,display,pronunciationhint,subtitle,image%29.md)
  Creates a custom intent object with the specified attributes.
- [init(identifier: String?, display: String, pronunciationHint: String?)](./init%28identifier,display,pronunciationhint%29.md)
  Creates a custom intent object with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobject/init(identifier:display:))*