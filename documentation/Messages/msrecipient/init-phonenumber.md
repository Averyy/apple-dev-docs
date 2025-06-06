# init(phoneNumber:)

**Framework**: Messages  
**Kind**: init

Creates a new critical message recipient with the provided phone number.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
init(phoneNumber: String)
```

#### Discussion

Use this method to create a new critical message recipient. When delivering messages, the framework displays the phone number you provide here.

> **Note**: If the framework can’t send a message due to an invalid phone number, the framework throws and [`MSCriticalMessagingError.sendFailed`](mscriticalmessagingerror/sendfailed.md) error.

If the framework can’t send a message due to an invalid phone number, the framework throws and [`MSCriticalMessagingError.sendFailed`](mscriticalmessagingerror/sendfailed.md) error.

## Parameters

- `phoneNumber`: A phone number that conforms to the  , without any non-numeric characters such as parentheses, periods, dashes, or a plus character (+) that introduces a country code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msrecipient/init(phonenumber:))*