# dispatchMessageToScript(withName:userInfo:)

**Framework**: Safari Services  
**Kind**: method

Dispatches a message from the app extension to the content script injected in this page.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func dispatchMessageToScript(withName messageName: String, userInfo: [String : Any]? = nil)
```

## Mentions

- [Adjusting settings for contextual menu items](adjusting-settings-for-contextual-menu-items.md)
- [Passing messages between Safari app extensions and injected scripts](passing-messages-between-safari-app-extensions-and-injected-scripts.md)

## Parameters

- `messageName`: A string that identifies the message.
- `userInfo`: An optional dictionary containing additional message content. If a dictionary is provided, values must conform to the W3C standard for safe passing of structured data, such as Boolean objects, numeric values, strings, and arrays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripage/dispatchmessagetoscript(withname:userinfo:))*