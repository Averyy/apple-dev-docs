# init()

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the get ride status intent object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Return Value

An initialized intent object or `nil` if the object could not be initialized.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user asks for the status of a ride. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintent/init())*