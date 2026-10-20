# nextAvailableURLs(withPathExtensions:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<NSURL *> *) nextAvailableURLsWithPathExtensions:(NSArray<NSString *> *) extensionArray error:(NSError **) outError;
```

#### Return Value

An array of digital camera format (DCF) compliant URLs with security scoping, one for each path extension element in `extensionArray`.

#### Discussion

The method generates a digital camera format (DCF) compliant URL with security scoping for each file extension element in `extensionArray`. It does this by configuring the folder structure and, if necessary, creates a digital camera image (DCIM) folder on the external storage device.

> ❗ **Important**:  The method generates an error if [`authorizationStatus`](./authorizationstatus.md) isn’t [`AVAuthorizationStatus.authorized`](../avauthorizationstatus/authorized.md).

##### Request access to the storage device before request

Your app can request authorization before calling the method if [`authorizationStatus`](./authorizationstatus.md) is [`AVAuthorizationStatus.notDetermined`](../avauthorizationstatus/notdetermined.md) by calling the [`requestAccess(completionHandler:)`](./requestaccess%28completionhandler%29.md) method first.

##### Start and stop access to a URL around your code

To access one of the security-scoped URLs the method returns, you need to call the [`startAccessingSecurityScopedResource()`](../../Foundation/url/startaccessingsecurityscopedresource%28%29.md), and [`stopAccessingSecurityScopedResource()`](../../Foundation/url/stopaccessingsecurityscopedresource%28%29.md) methods before and after your code.

**Swift**:

```swift
securityScopedURL.startAccessingSecurityScopedResource()

// Your code that accesses the URL goes in between the start and stop calls.
...

securityScopedURL.stopAccessingSecurityScopedResource()
```

**Objective-C**:

```objc
[securityScopedURL startAccessingSecurityScopedResource];

// Your code that accesses the URL goes in between the start and stop calls.
...

[securityScopedURL stopAccessingSecurityScopedResource];

```

## Parameters

- `extensionArray`: An array of path extensions the method generates URLs for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice/nextavailableurls(withpathextensions:))*