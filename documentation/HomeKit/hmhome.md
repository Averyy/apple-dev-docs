# HMHome

**Framework**: HomeKit  
**Kind**: class

The primary unit of living space, typically composed of rooms organized into zones.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMHome
```

#### Overview

An [`HMHome`](hmhome.md) instance is a top-level container in HomeKit representing a structure that a user considers as a single home. Users might have multiple homes that are far apart, like a primary home and a vacation home. Or they might have two homes that are close together, but that they consider as distinct units—for example, a main home and a guest cottage on the same property.

An [`HMHome`](hmhome.md) instance:

- Is the main access point for communicating with and configuring accessories, like a garage door opener or a thermostat.
- Organizes accessories into a number of rooms, which are themselves optionally grouped into zones, such as the upstairs.
- Allows the user to define sets of actions that can be performed with a single operation, and triggers that cause an action set to be performed at a specific time.

You create a new home only in response to a specific user request, but you don’t do it directly. When the user asks your app to create a new home—for example, by tapping an Add button in your interface—your app calls the home manager’s [`addHome(withName:completionHandler:)`](hmhomemanager/addhome(withname:completionhandler:).md) method with a name that the user supplies. To get a list of existing home instances, use the [`homes`](hmhomemanager/homes.md) array of the home manager (an instance of [`HMHomeManager`](hmhomemanager.md)).

Because HomeKit gives your app access to a shared database of home automation information, other apps can change the home’s configuration. Adopt the [`HMHomeDelegate`](hmhomedelegate.md) protocol in your app to stay informed of any such changes that happen outside your app.

## Topics

### Keeping track of home configuration changes
- [var delegate: (any HMHomeDelegate)?](hmhome/delegate.md)
  A delegate that receives updates on the state of the home.
- [protocol HMHomeDelegate](hmhomedelegate.md)
  An interface that communicates changes to a home’s configuration.
### Identifying a home
- [var name: String](hmhome/name.md)
  The name the user gives to the home.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](hmhome/updatename(_:completionhandler:).md)
  Updates the name of the home.
- [var uniqueIdentifier: UUID](hmhome/uniqueidentifier.md)
  A unique identifier for the home.
- [var isPrimary: Bool](hmhome/isprimary.md)
  A Boolean value that indicates whether this is the primary home for its home manager.
### Dividing a house into rooms
- [var rooms: [HMRoom]](hmhome/rooms.md)
  An array of the rooms created and managed by the user.
- [func roomForEntireHome() -> HMRoom](hmhome/roomforentirehome.md)
  A room that represents all parts of the home that don’t have a more specific room to represent them.
- [func addRoom(withName: String, completionHandler: (HMRoom?, (any Error)?) -> Void)](hmhome/addroom(withname:completionhandler:).md)
  Creates a new room with the specified name.
- [func removeRoom(HMRoom, completionHandler: ((any Error)?) -> Void)](hmhome/removeroom(_:completionhandler:).md)
  Removes a room from the home.
- [class HMRoom](hmroom.md)
  The smallest subdivision of a home’s space.
### Grouping rooms into zones
- [var zones: [HMZone]](hmhome/zones.md)
  An array of all the zones in the home.
- [func addZone(withName: String, completionHandler: (HMZone?, (any Error)?) -> Void)](hmhome/addzone(withname:completionhandler:).md)
  Adds a new zone to the home.
- [func removeZone(HMZone, completionHandler: ((any Error)?) -> Void)](hmhome/removezone(_:completionhandler:).md)
  Removes a zone from the home.
- [class HMZone](hmzone.md)
  A collection of rooms that users think of as a single area, like upstairs or downstairs.
### Managing accessories
- [var accessories: [HMAccessory]](hmhome/accessories.md)
  The collection of accessories that are part of the home.
- [func addAndSetupAccessories(completionHandler: ((any Error)?) -> Void)](hmhome/addandsetupaccessories(completionhandler:).md)
  Finds and adds nearby accessories to the home.
- [func addAndSetupAccessories(with: HMAccessorySetupPayload, completionHandler: ([HMAccessory]?, (any Error)?) -> Void)](hmhome/addandsetupaccessories(with:completionhandler:).md)
  Finds and adds nearby accessories to the home using a HomeKit code provided by your app.
- [func addAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](hmhome/addaccessory(_:completionhandler:).md)
  Adds a new accessory to the home.
- [func assignAccessory(HMAccessory, to: HMRoom, completionHandler: ((any Error)?) -> Void)](hmhome/assignaccessory(_:to:completionhandler:).md)
  Assigns an accessory to a different room.
- [func removeAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](hmhome/removeaccessory(_:completionhandler:).md)
  Removes an accessory from the home.
- [var supportsAddingNetworkRouter: Bool](hmhome/supportsaddingnetworkrouter.md)
  A Boolean that indicates whether a home supports all of the requirements for adding a network router.
- [func unblockAccessory(HMAccessory, completionHandler: ((any Error)?) -> Void)](hmhome/unblockaccessory(_:completionhandler:).md)
  Unblocks a blocked accessory.
- [class HMAccessory](hmaccessory.md)
  A home automation accessory, like a garage door opener or a thermostat.
### Grouping services
- [func servicesWithTypes([String]) -> [HMService]?](hmhome/serviceswithtypes(_:).md)
  Returns an array of all services provided by accessories in the home that match the specified types.
- [var serviceGroups: [HMServiceGroup]](hmhome/servicegroups.md)
  An array of all service groups in the home.
- [func addServiceGroup(withName: String, completionHandler: (HMServiceGroup?, (any Error)?) -> Void)](hmhome/addservicegroup(withname:completionhandler:).md)
  Adds a service group to the home.
- [func removeServiceGroup(HMServiceGroup, completionHandler: ((any Error)?) -> Void)](hmhome/removeservicegroup(_:completionhandler:).md)
  Removes a service group from the home.
- [class HMServiceGroup](hmservicegroup.md)
  A collection of accessory services.
### Querying the state of a home hub
- [var homeHubState: HMHomeHubState](hmhome/homehubstate.md)
  The state of the home hub.
- [enum HMHomeHubState](hmhomehubstate.md)
  The possible states of the home hub.
### Creating action sets
- [var actionSets: [HMActionSet]](hmhome/actionsets.md)
  An array of the action sets in the home.
- [func addActionSet(withName: String, completionHandler: (HMActionSet?, (any Error)?) -> Void)](hmhome/addactionset(withname:completionhandler:).md)
  Adds a new action set to the home.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmhome/removeactionset(_:completionhandler:).md)
  Removes an action set from the home.
- [func executeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmhome/executeactionset(_:completionhandler:).md)
  Executes all the actions in a specified action set.
- [func builtinActionSet(ofType: String) -> HMActionSet?](hmhome/builtinactionset(oftype:).md)
  Retrieves the builtin action set for the specified type.
- [class HMActionSet](hmactionset.md)
  A collection of actions that you trigger as a group.
### Triggering an action set
- [var triggers: [HMTrigger]](hmhome/triggers.md)
  An array of triggers defined in the home.
- [func addTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](hmhome/addtrigger(_:completionhandler:).md)
  Adds a trigger to the home.
- [func removeTrigger(HMTrigger, completionHandler: ((any Error)?) -> Void)](hmhome/removetrigger(_:completionhandler:).md)
  Removes a trigger from the home.
- [class HMTimerTrigger](hmtimertrigger.md)
  A trigger to activate an action set based on a periodic timer.
- [class HMEventTrigger](hmeventtrigger.md)
  A trigger to activate an action set based on a set of events and optional conditions.
- [class HMTrigger](hmtrigger.md)
  An abstract base class for triggering actions based on a set of conditions.
### Managing users
- [func manageUsers(completionHandler: ((any Error)?) -> Void)](hmhome/manageusers(completionhandler:).md)
  Presents a view controller to manage users of the home.
- [var currentUser: HMUser](hmhome/currentuser.md)
  The current HomeKit user.
- [class HMUser](hmuser.md)
  A person in the home who may have access to control accessories and services in the home.
### Controlling user access
- [func homeAccessControl(for: HMUser) -> HMHomeAccessControl](hmhome/homeaccesscontrol(for:).md)
  Retrieves the access level of a user associated with the home.
- [class HMHomeAccessControl](hmhomeaccesscontrol.md)
  The access privileges of a user associated with a home.
- [class HMAccessControl](hmaccesscontrol.md)
  An abstract superclass for accessing user privileges.
- [let HMUserFailedAccessoriesKey: String](hmuserfailedaccessorieskey.md)
  The key for retrieving details of what accessories failed to add or remove a user.
### Deprecated symbols
- [var users: [HMUser]](hmhome/users.md)
  All users associated with the home.
- [func addUser(completionHandler: (HMUser?, (any Error)?) -> Void)](hmhome/adduser(completionhandler:).md)
  Adds a user to the home.
- [func removeUser(HMUser, completionHandler: ((any Error)?) -> Void)](hmhome/removeuser(_:completionhandler:).md)
  Removes a user from the home.
### Instance Properties
- [var matterControllerID: String](hmhome/mattercontrollerid.md)
- [var matterControllerXPCConnectBlock: () -> NSXPCConnection](hmhome/mattercontrollerxpcconnectblock.md)
- [var matterStartupParametersXPCConnectBlock: () -> NSXPCConnection](hmhome/matterstartupparametersxpcconnectblock.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var homes: [HMHome]](hmhomemanager/homes.md)
  An array of all homes managed by this home manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome)*