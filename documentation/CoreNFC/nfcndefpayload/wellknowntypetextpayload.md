# wellKnownTypeTextPayload()

**Framework**: Core NFC  
**Kind**: method

Returns the text and locale of a valid Well Known Type Text payload.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+

## Declaration

```swift
func wellKnownTypeTextPayload() -> (String?, Locale?)
```

#### Return Value

A tuple containing a string and locale from a Well Known Type Text payload. The string and locale can be `nil`.

#### Discussion

Use this method to get option text from a text payload.

```swift
// Get the optional informational text from the text payload.
var additionInfo: String? = nil

for payload in message.records {
    (additionInfo, _) = payload.wellKnownTypeTextPayload()
    
    if additionInfo != nil {
        break
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/wellknowntypetextpayload())*