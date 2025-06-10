# Core Telephony

**Framework**: Core Telephony  
**Kind**: module

Access information about a user’s cellular service provider, such as its unique identifier and whether the carrier allows VoIP.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.10+

#### Overview

Use the Core Telephony framework to obtain information about a user’s home cellular service provider. Carriers can use this information to write apps that provide services only for their own subscribers. You can also use this framework to obtain information about current cellular calls.

A [`CTCarrier`](ctcarrier.md) object gives you information about the user’s cellular service provider, such as whether it allows use of VoIP (Voice over Internet Protocol) on its network. A [`CTCall`](ctcall.md) object gives you information about a current call, including a unique identifier and state information such as dialing, incoming, connected, or disconnected.

> **Note**:  VoIP and cellular services through Core Telephony are unavailable for compatible iPad and iPhone apps running in visionOS. You can still use the APIs of this framework, but services don’t return carrier information.

## Topics

### Service Information
- [class CTTelephonyNetworkInfo](cttelephonynetworkinfo.md)
  An object that provides notifications of changes to the user’s cellular service provider.
### eSIM
- [class CTCellularPlanProvisioning](ctcellularplanprovisioning.md)
  An object you use to download and install a carrier eSIM.
- [class CTCellularPlanProvisioningRequest](ctcellularplanprovisioningrequest.md)
  A request specifying an eSIM to download and install.
- [class CTCellularPlanProperties](ctcellularplanproperties.md)
  An object you use for an eSIM.
- [enum CTCellularPlanCapability](ctcellularplancapability.md)
  The type of cellular plan available for an eSIM.
### SIM
- [class CTCellularPlanStatus](ctcellularplanstatus.md)
  An object used for retrieving and checking the validity of a token.
### Subscriber Information
- [class CTSubscriber](ctsubscriber.md)
  A cellular network subscriber.
- [protocol CTSubscriberDelegate](ctsubscriberdelegate.md)
  A protocol to handle changes to subscriber information.
- [class CTSubscriberInfo](ctsubscriberinfo.md)
  An object that provides an array of cellular network subscribers.
### Cellular Data Access
- [class CTCellularData](ctcellulardata.md)
  An object indicating whether the app can access cellular data.
### Errors
- [struct CTError](cterror.md)
  A type representing a Core Telephony error.
### Deprecated
- [class CTCarrier](ctcarrier.md)
  Information about the user’s cellular service provider, such as its unique identifier and whether it allows VoIP calls on its network.
- [class CTCall](ctcall.md)
  An object used to identify a cellular call and determine its state.
- [class CTCallCenter](ctcallcenter.md)
  An object that provides a list of current cellular calls, and provides the ability to respond to state changes for calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreTelephony)*