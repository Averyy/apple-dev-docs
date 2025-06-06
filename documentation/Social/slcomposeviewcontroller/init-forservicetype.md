# init(forServiceType:)

**Framework**: Social  
**Kind**: init

Creates a new social compose view controller.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init!(forServiceType serviceType: String!)
```

#### Return Value

Returns a social compose view controller or `nil` if an error occurs.

#### Discussion

Use this method to create a social compose view controller. Do not use any other methods.

## Parameters

- `serviceType`: This specifies the social networking service to which you want to post. You must use one of the possible values listed in Service Type Constants. This also sets the value of  . If an invalid   is passed in, this method throws an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposeviewcontroller/init(forservicetype:))*