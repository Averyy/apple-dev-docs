# prepare(for:)

**Framework**: IdentityLookupUI  
**Kind**: method  
**Role**: Instance Method

Notifies the view controller just before the system presents it to the user.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
func prepare(for request: ILClassificationRequest)
```

```objc
- (void) prepareForClassificationRequest:(ILClassificationRequest *) request;
```

## See Also

### Collecting Data from the User
- [func classificationResponse(for: ILClassificationRequest) -> ILClassificationResponse](./classificationresponse%28for%29.md)
  Notifies the view controller when the user finishes entering data and presses the Done button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller/prepare(for:))*