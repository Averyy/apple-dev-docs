# classificationResponse(for:)

**Framework**: IdentityLookupUI  
**Kind**: method  
**Role**: Instance Method

Notifies the view controller when the user finishes entering data and presses the Done button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
func classificationResponse(for request: ILClassificationRequest) -> ILClassificationResponse
```

```objc
- (ILClassificationResponse *) classificationResponseForRequest:(ILClassificationRequest *) request;
```

## See Also

### Collecting Data from the User
- [func prepare(for: ILClassificationRequest)](./prepare%28for%29.md)
  Notifies the view controller just before the system presents it to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller/classificationresponse(for:))*