# SFAddToHomeScreenInfo

**Framework**: Safari Services  
**Kind**: class  
**Role**: Class

A class that provides information about a web app that someone adds to their Home Screen.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- visionOS 2.2+

## Declaration

```swift
class SFAddToHomeScreenInfo
```

```objc
@interface SFAddToHomeScreenInfo : NSObject
```

## Overview

Create an instance of `SFAddToHomeScreenInfo` in your [`getHomeScreenWebAppInfo(completionHandler:)`](./sfaddtohomescreenactivityitem/gethomescreenwebappinfo%28completionhandler%29.md) implementation. Configure the object with the web app’s manifest and the cookies your browser uses with the web app, then pass the object to the method’s completion handler.

## Topics

### Creating an information object
- [init(manifest: BEWebAppManifest)](./sfaddtohomescreeninfo/init%28manifest%29.md)
  Initializes a Home Screen information object with the supplied web app manifest.
### Information about a web app
- [var manifest: BEWebAppManifest](./sfaddtohomescreeninfo/manifest.md)
- [var websiteCookies: [HTTPCookie]](./sfaddtohomescreeninfo/websitecookies.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Providing information about a web app to the system
- [func getHomeScreenWebAppInfo(completionHandler: (SFAddToHomeScreenInfo?) -> Void)](./sfaddtohomescreenactivityitem/gethomescreenwebappinfo%28completionhandler%29.md)
  Provides information about a web app to the system.
- [func getWebAppManifest(completionHandler: (BEWebAppManifest?) -> Void)](./sfaddtohomescreenactivityitem/getwebappmanifest%28completionhandler%29.md)
  Provides the web app’s manifest to the system, if the bookmark represents a web app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfaddtohomescreeninfo)*