# nextAvailableURLs(withPathExtensions:)

**Framework**: AVFoundation  
**Kind**: method

Generates an array of security scoped URLs that are compliant for digital camera formats, where each element has a different path extension.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func nextAvailableURLs(withPathExtensions extensionArray: [String]) throws -> [URL]
```

#### Return Value

An array of digital camera format (DCF) compliant URLs with security scoping, one for each path extension element in `extensionArray`.

#### Discussion

The method generates a digital camera format (DCF) compliant URL with security scoping for each file extension element in `extensionArray`. It does this by configuring the folder structure and, if necessary, creates a digital camera image (DCIM) folder on the external storage device.

> ❗ **Important**:  The method generates an error if [`authorizationStatus`](avexternalstoragedevice/authorizationstatus.md) isn’t [`AVAuthorizationStatus.authorized`](avauthorizationstatus/authorized.md).

##### Request Access to the Storage Device Before Request

Your app can request authorization before calling the method if [`authorizationStatus`](avexternalstoragedevice/authorizationstatus.md) is [`AVAuthorizationStatus.notDetermined`](avauthorizationstatus/notdetermined.md) by calling the [`requestAccess(completionHandler:)`](avexternalstoragedevice/requestaccess(completionhandler:).md) method first.

##### Start and Stop Access to a Url Around Your Code

To access one of the security-scoped URLs the method returns, you need to call the [`startAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/Foundation/URL/startAccessingSecurityScopedResource()), and [`stopAccessingSecurityScopedResource()`](https://developer.apple.com/documentation/Foundation/URL/stopAccessingSecurityScopedResource()) methods before and after your code.

## Parameters

- `extensionArray`: An array of path extensions the method generates URLs for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/nextavailableurls(withpathextensions:))*