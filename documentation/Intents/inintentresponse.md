# INIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your response to an intent object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INIntentResponse
```

```objc
@interface INIntentResponse : NSObject
```

## Overview

The [`INIntentResponse`](./inintentresponse.md) class is abstract and provides common behavior for all response objects that your app creates. You do not create instances of this class directly. Instead, you create instances of the specific subclasses representing the intents that you are trying to handle. This class provides access to the custom user activity object that you provided when initializing your response object.

## Topics

### Accessing the User Activity Object
- [var userActivity: NSUserActivity?](./inintentresponse/useractivity.md)
  The user activity object to use when launching the app.
### Initializers
- [init?(coder: NSCoder)](./inintentresponse/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [INActivateCarSignalIntentResponse](./inactivatecarsignalintentresponse.md)
- [INAddMediaIntentResponse](./inaddmediaintentresponse.md)
- [INAddTasksIntentResponse](./inaddtasksintentresponse.md)
- [INAnswerCallIntentResponse](./inanswercallintentresponse.md)
- [INAppendToNoteIntentResponse](./inappendtonoteintentresponse.md)
- [INBookRestaurantReservationIntentResponse](./inbookrestaurantreservationintentresponse.md)
- [INCancelRideIntentResponse](./incancelrideintentresponse.md)
- [INCancelWorkoutIntentResponse](./incancelworkoutintentresponse.md)
- [INCreateNoteIntentResponse](./increatenoteintentresponse.md)
- [INCreateTaskListIntentResponse](./increatetasklistintentresponse.md)
- [INDeleteTasksIntentResponse](./indeletetasksintentresponse.md)
- [INEditMessageIntentResponse](./ineditmessageintentresponse.md)
- [INEndWorkoutIntentResponse](./inendworkoutintentresponse.md)
- [INGetAvailableRestaurantReservationBookingDefaultsIntentResponse](./ingetavailablerestaurantreservationbookingdefaultsintentresponse.md)
- [INGetAvailableRestaurantReservationBookingsIntentResponse](./ingetavailablerestaurantreservationbookingsintentresponse.md)
- [INGetCarLockStatusIntentResponse](./ingetcarlockstatusintentresponse.md)
- [INGetCarPowerLevelStatusIntentResponse](./ingetcarpowerlevelstatusintentresponse.md)
- [INGetReservationDetailsIntentResponse](./ingetreservationdetailsintentresponse.md)
- [INGetRestaurantGuestIntentResponse](./ingetrestaurantguestintentresponse.md)
- [INGetRideStatusIntentResponse](./ingetridestatusintentresponse.md)
- [INGetUserCurrentRestaurantReservationBookingsIntentResponse](./ingetusercurrentrestaurantreservationbookingsintentresponse.md)
- [INGetVisualCodeIntentResponse](./ingetvisualcodeintentresponse.md)
- [INHangUpCallIntentResponse](./inhangupcallintentresponse.md)
- [INListCarsIntentResponse](./inlistcarsintentresponse.md)
- [INListRideOptionsIntentResponse](./inlistrideoptionsintentresponse.md)
- [INPauseWorkoutIntentResponse](./inpauseworkoutintentresponse.md)
- [INPayBillIntentResponse](./inpaybillintentresponse.md)
- [INPlayMediaIntentResponse](./inplaymediaintentresponse.md)
- [INRequestPaymentIntentResponse](./inrequestpaymentintentresponse.md)
- [INRequestRideIntentResponse](./inrequestrideintentresponse.md)
- [INResumeWorkoutIntentResponse](./inresumeworkoutintentresponse.md)
- [INSaveProfileInCarIntentResponse](./insaveprofileincarintentresponse.md)
- [INSearchCallHistoryIntentResponse](./insearchcallhistoryintentresponse.md)
- [INSearchForAccountsIntentResponse](./insearchforaccountsintentresponse.md)
- [INSearchForBillsIntentResponse](./insearchforbillsintentresponse.md)
- [INSearchForMediaIntentResponse](./insearchformediaintentresponse.md)
- [INSearchForMessagesIntentResponse](./insearchformessagesintentresponse.md)
- [INSearchForNotebookItemsIntentResponse](./insearchfornotebookitemsintentresponse.md)
- [INSearchForPhotosIntentResponse](./insearchforphotosintentresponse.md)
- [INSendMessageIntentResponse](./insendmessageintentresponse.md)
- [INSendPaymentIntentResponse](./insendpaymentintentresponse.md)
- [INSendRideFeedbackIntentResponse](./insendridefeedbackintentresponse.md)
- [INSetAudioSourceInCarIntentResponse](./insetaudiosourceincarintentresponse.md)
- [INSetCarLockStatusIntentResponse](./insetcarlockstatusintentresponse.md)
- [INSetClimateSettingsInCarIntentResponse](./insetclimatesettingsincarintentresponse.md)
- [INSetDefrosterSettingsInCarIntentResponse](./insetdefrostersettingsincarintentresponse.md)
- [INSetMessageAttributeIntentResponse](./insetmessageattributeintentresponse.md)
- [INSetProfileInCarIntentResponse](./insetprofileincarintentresponse.md)
- [INSetRadioStationIntentResponse](./insetradiostationintentresponse.md)
- [INSetSeatSettingsInCarIntentResponse](./insetseatsettingsincarintentresponse.md)
- [INSetTaskAttributeIntentResponse](./insettaskattributeintentresponse.md)
- [INShareFocusStatusIntentResponse](./insharefocusstatusintentresponse.md)
- [INSnoozeTasksIntentResponse](./insnoozetasksintentresponse.md)
- [INStartAudioCallIntentResponse](./instartaudiocallintentresponse.md)
- [INStartCallIntentResponse](./instartcallintentresponse.md)
- [INStartPhotoPlaybackIntentResponse](./instartphotoplaybackintentresponse.md)
- [INStartVideoCallIntentResponse](./instartvideocallintentresponse.md)
- [INStartWorkoutIntentResponse](./instartworkoutintentresponse.md)
- [INTransferMoneyIntentResponse](./intransfermoneyintentresponse.md)
- [INUnsendMessagesIntentResponse](./inunsendmessagesintentresponse.md)
- [INUpdateMediaAffinityIntentResponse](./inupdatemediaaffinityintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Intents
- [Dispatching intents to handlers](../SiriKit/dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Resolving and Handling Intents](../SiriKit/resolving-and-handling-intents.md)
  Resolve, confirm, and handle user requests for your app’s services.
- [class INIntent](./inintent.md)
  A request to fulfill in your app or Intents extension.
- [Intent Handling Infrastructure](../SiriKit/intent-handling-infrastructure.md)
  Specify required permissions and provide handlers for the intents your app supports, and configure app extensions.
- [Providing Hands-Free App Control with Intents](../SiriKit/providing-hands-free-app-control-with-intents.md)
  Resolve, confirm, and handle intents without an extension.
- [Resolution Results](../SiriKit/resolution-results.md)
  Resolve common types of data like strings and dates into specific values that your app recognizes.
- [Common Data Types](../SiriKit/common-data-types.md)
  Manage common data types such as strings, dates, currencies, images, and contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintentresponse)*