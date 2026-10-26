# init(identifier:display:pronunciationHint:subtitle:image:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a custom intent object with the specified attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(identifier: String?, display displayString: String, pronunciationHint: String?, subtitle subtitleString: String?, image displayImage: INImage?)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier displayString:(NSString *) displayString pronunciationHint:(NSString *) pronunciationHint subtitleString:(NSString *) subtitleString displayImage:(INImage *) displayImage;
```

#### Return Value

A new [`INObject`](../inobject.md), or `nil` if the initializer couldn’t create the object.

## Parameters

- `identifier`: A string that identifies the custom object within your app.
- `displayString`: A string that concisely describes the custom object.
- `pronunciationHint`: A pronunciation hint for the custom object.
- `subtitleString`: A string that adds secondary information about the object.
- `displayImage`: An image representing the object.

## See Also

### Creating a Custom Object
- [convenience init(identifier: String?, display: String, subtitle: String?, image: INImage?)](./init%28identifier,display,subtitle,image%29.md)
  Creates a custom intent object with full display information.
- [convenience init(identifier: String?, display: String)](./init%28identifier,display%29.md)
  Creates a custom intent object with the specified identifier and display string.
- [init(identifier: String?, display: String, pronunciationHint: String?)](./init%28identifier,display,pronunciationhint%29.md)
  Creates a custom intent object with the specified attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobject/init(identifier:display:pronunciationhint:subtitle:image:))*