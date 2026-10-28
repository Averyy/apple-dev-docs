# Authorization Plug-ins

**Framework**: Security  
**Role**: API Collection

Extend the authorization services API by creating plug-ins that can participate in authorization decisions.

## Overview

Use plug-ins to extend macOS authorization services to perform authorizations in a new way or to implement a new policy that is too complex to be implemented entirely with the authorization policy database.

You must import this API explicitly:

**Swift**:

```swift
import Security.AuthorizationPlugin
```

**Objective-C**:

```objc
#import <Security/AuthorizationPlugin.h>       
```

> **Note**:  When your plug-in needs to interact with the user, subclass the [`SFAuthorizationPluginView`](../SecurityInterface/sfauthorizationpluginview.md) class to maintain the look and feel of the system authentication dialogs.

## Topics

### First Steps
- [Extending authorization services with plug-ins](./extending-authorization-services-with-plug-ins.md)
  Modify the system’s authorization policy with custom code.
### Creating a Plug-in
- [AuthorizationCallbacks Version](./authorizationcallbacks-version.md)
  The version of the interface implemented by the authorization engine.
- [AuthorizationPluginInterface Version](./authorizationplugininterface-version.md)
  The version of the interface implemented by the plug-in.
- [AuthorizationPluginCreate](./authorizationplugincreate.md)
  Initializes the plug-in and exchanges interfaces with the authorization engine.
- [AuthorizationPluginRef](./authorizationpluginref.md)
  A handle passed by the plug-in to the authorization engine when the plug-in is initiated.
- [AuthorizationCallbacks](./authorizationcallbacks.md)
  The interface implemented by the Security Server.
- [AuthorizationPluginInterface](./authorizationplugininterface.md)
  The interface that must be implemented by your plug-in.
### Supporting Types and Constants
- [AuthorizationValue](./authorizationvalue.md)
  A structure used to pass data between the authorization engine and the plug-in mechanism.
- [AuthorizationValueVector](./authorizationvaluevector.md)
  A structure used to pass arguments from the authorization policy database to the authorization mechanism.
- [AuthorizationMechanismId](./authorizationmechanismid.md)
  The mechanism ID specified in the authorization policy database is passed to the plug-in to create the appropriate mechanism.
- [AuthorizationPluginId](./authorizationpluginid.md)
  An unused identifier for a plug-in.
- [AuthorizationMechanismRef](./authorizationmechanismref.md)
  A handle passed by the plug-in to the authorization engine when creating an instance of a mechanism.
- [AuthorizationEngineRef](./authorizationengineref.md)
  Handle passed from the authorization engine to an instance of a mechanism in a plug-in.
- [AuthorizationSessionId](./authorizationsessionid.md)
  A unique value for an authorization session, provided by the authorization engine.
- [AuthorizationResult](./authorizationresult.md)
  The permissible values for an authorization evaluation result.
- [AuthorizationContextFlags](./authorizationcontextflags.md)
  The flags that specify whether authentication data should be made available to the authorization client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorization-plug-ins)*