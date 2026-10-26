# Deprecated Symbols

**Framework**: SiriKit  
**Role**: API Collection

Review unsupported symbols and their replacements.

#### Overview

Many deprecated system intents have no replacement. You may continue to provide these features by defining custom intents. For more information about custom intents, see [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](./adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md).

## Topics

### Audio Call Initiation
- [protocol INStartAudioCallIntentHandling](../Intents/instartaudiocallintenthandling.md)
  The handler interface for initiating an audio call from your app.
- [class INStartAudioCallIntent](../Intents/instartaudiocallintent.md)
  A request to start an audio-only call with one or more users.
- [class INStartAudioCallIntentResponse](../Intents/instartaudiocallintentresponse.md)
  An app’s response to an intent to start an audio call.
### Video Call Initiation
- [protocol INStartVideoCallIntentHandling](../Intents/instartvideocallintenthandling.md)
  The handler interface for initiating a video call from your app.
- [class INStartVideoCallIntent](../Intents/instartvideocallintent.md)
  A request to start a video call with one or more users.
- [class INStartVideoCallIntentResponse](../Intents/instartvideocallintentresponse.md)
  A response to an intent to start a video call.
### Note Content
- [enum INNoteContentType](../Intents/innotecontenttype.md)
  Constants indicating the type of content represented by the note.
- [class INNoteContentTypeResolutionResult](../Intents/innotecontenttyperesolutionresult.md)
  A resolution result for the type of data contained in notes.
### Domain-Handling Protocols
- [protocol INMessagesDomainHandling](../Intents/inmessagesdomainhandling.md)
  An interface for adopting all of the protocols in the messages domain.
- [protocol INNotebookDomainHandling](../Intents/innotebookdomainhandling.md)
  An interface for adopting all of the protocols in the lists and notes domain.
- [protocol INWorkoutsDomainHandling](../Intents/inworkoutsdomainhandling.md)
  An interface for adopting all of the protocols in the workouts domain.
- [protocol INPaymentsDomainHandling](../Intents/inpaymentsdomainhandling.md)
  An interface for adopting all of the protocols in the payments domain.
- [protocol INCallsDomainHandling](../Intents/incallsdomainhandling.md)
  Provides a convenient way to adopt all of the protocols in the VoIP calling domain.
- [protocol INVisualCodeDomainHandling](../Intents/invisualcodedomainhandling.md)
  An interface for adopting all of the protocols in the visual codes domain.
- [protocol INPhotosDomainHandling](../Intents/inphotosdomainhandling.md)
  An interface for adopting all of the protocols in the photos domain.
- [protocol INRidesharingDomainHandling](../Intents/inridesharingdomainhandling.md)
  An interface for adopting all of the protocols in the ride-booking domain.
- [protocol INCarCommandsDomainHandling](../Intents/incarcommandsdomainhandling.md)
  An interface for adopting all the handling protocols in the car commands domain.
- [protocol INCarPlayDomainHandling](../Intents/incarplaydomainhandling.md)
  An interface for adopting all of the protocols in the CarPlay domain.
- [protocol INRadioDomainHandling](../Intents/inradiodomainhandling.md)
  An interface for adopting all of the protocols in the radio domain.
### Bill Payment
- [protocol INPayBillIntentHandling](../Intents/inpaybillintenthandling.md)
  The handler interface for paying a bill using money from the user’s account.
- [class INPayBillIntent](../Intents/inpaybillintent.md)
  A request to transfer money to facilitate payment of a bill.
- [class INPayBillIntentResponse](../Intents/inpaybillintentresponse.md)
  Your app’s response to a request to pay a bill.
### Bill Search
- [protocol INSearchForBillsIntentHandling](../Intents/insearchforbillsintenthandling.md)
  The handler interface for searching for bills associated with the user.
- [class INSearchForBillsIntent](../Intents/insearchforbillsintent.md)
  A request for the list of bills matching the specified criteria.
- [class INSearchForBillsIntentResponse](../Intents/insearchforbillsintentresponse.md)
  Your app’s response to a request to a search for bills.
### Bill Data Objects
- [class INBillDetails](../Intents/inbilldetails.md)
  The detailed information associated with a bill.
- [class INBillPayee](../Intents/inbillpayee.md)
  The entity that receives the proceeds from a bill payment.
- [class INBillTypeResolutionResult](../Intents/inbilltyperesolutionresult.md)
  A resolution result for the types of bills a user might pay.
- [class INBillPayeeResolutionResult](../Intents/inbillpayeeresolutionresult.md)
  A resolution result for the recipient of a bill payment.
- [class INVisualCodeTypeResolutionResult](../Intents/invisualcodetyperesolutionresult.md)
  A resolution result for the type of visual code used to exchange information.
### Call History Search
- [protocol INSearchCallHistoryIntentHandling](../Intents/insearchcallhistoryintenthandling.md)
  The handler interface for searching the user’s call history.
- [class INSearchCallHistoryIntent](../Intents/insearchcallhistoryintent.md)
  A request to list the calls matching the specified criteria.
- [class INSearchCallHistoryIntentResponse](../Intents/insearchcallhistoryintentresponse.md)
  Your app’s response to a search call history intent.
### CarPlay Audio Source
- [protocol INSetAudioSourceInCarIntentHandling](../Intents/insetaudiosourceincarintenthandling.md)
  The handler interface for changing a vehicle’s audio source.
- [class INSetAudioSourceInCarIntent](../Intents/insetaudiosourceincarintent.md)
  A request to change the source of audio playback in a CarPlay-enabled vehicle.
- [class INSetAudioSourceInCarIntentResponse](../Intents/insetaudiosourceincarintentresponse.md)
  Your app’s response to a set audio source in car intent.
### CarPlay Climate Settings
- [protocol INSetClimateSettingsInCarIntentHandling](../Intents/insetclimatesettingsincarintenthandling.md)
  The handler interface for changing a vehicle’s climate control settings.
- [class INSetClimateSettingsInCarIntent](../Intents/insetclimatesettingsincarintent.md)
  A request to change the climate settings in a CarPlay-enabled vehicle.
- [class INSetClimateSettingsInCarIntentResponse](../Intents/insetclimatesettingsincarintentresponse.md)
  Your app’s response to a set climate settings in car intent.
### CarPlay Defroster Settings
- [protocol INSetDefrosterSettingsInCarIntentHandling](../Intents/insetdefrostersettingsincarintenthandling.md)
  The handler interface for changing a vehicle’s defroster settings.
- [class INSetDefrosterSettingsInCarIntent](../Intents/insetdefrostersettingsincarintent.md)
  A request to change the defroster settings in a CarPlay-enabled vehicle.
- [class INSetDefrosterSettingsInCarIntentResponse](../Intents/insetdefrostersettingsincarintentresponse.md)
  Your app’s response to a set defroster settings in car intent.
### CarPlay Profile Saving
- [protocol INSaveProfileInCarIntentHandling](../Intents/insaveprofileincarintenthandling.md)
  The handler interface for saving vehicle environment settings to a user-specified profile.
- [class INSaveProfileInCarIntent](../Intents/insaveprofileincarintent.md)
  A request to save the user’s vehicle environment settings in a CarPlay-enabled vehicle.
- [class INSaveProfileInCarIntentResponse](../Intents/insaveprofileincarintentresponse.md)
  Your app’s response to a save profile in car intent.
### CarPlay Profile Settings
- [protocol INSetProfileInCarIntentHandling](../Intents/insetprofileincarintenthandling.md)
  The handler interface for restoring vehicle environment settings from a user-specified profile.
- [class INSetProfileInCarIntent](../Intents/insetprofileincarintent.md)
  A request to change the user’s vehicle environment settings to the ones from the specified profile.
- [class INSetProfileInCarIntentResponse](../Intents/insetprofileincarintentresponse.md)
  Your app’s response to a set profile in car intent.
### CarPlay Radio Station Settings
- [protocol INSetRadioStationIntentHandling](../Intents/insetradiostationintenthandling.md)
  The handler interface for changing a radio station.
- [class INSetRadioStationIntent](../Intents/insetradiostationintent.md)
  A request to change the current radio station.
- [class INSetRadioStationIntentResponse](../Intents/insetradiostationintentresponse.md)
  Your app’s response to a set radio station intent.
### CarPlay Seat Settings
- [protocol INSetSeatSettingsInCarIntentHandling](../Intents/insetseatsettingsincarintenthandling.md)
  The handler interface for changing a vehicle’s seat-related settings.
- [class INSetSeatSettingsInCarIntent](../Intents/insetseatsettingsincarintent.md)
  A request to change the seat-related settings in a CarPlay-enabled vehicle.
- [class INSetSeatSettingsInCarIntentResponse](../Intents/insetseatsettingsincarintentresponse.md)
  Your app’s response to a set seat settings in car intent.
### CarPlay Data Objects
- [enum INCarSeat](../Intents/incarseat.md)
  Constants indicating a seat position.
- [enum INCarDefroster](../Intents/incardefroster.md)
  Constants indicating the defroster type.
- [enum INCarAudioSource](../Intents/incaraudiosource.md)
  Constants indicating the source of audio.
- [enum INCarAirCirculationMode](../Intents/incaraircirculationmode.md)
  Constants indicating the circulation mode for the climate system.
- [enum INRadioType](../Intents/inradiotype.md)
  Constants indicating the type of radio.
- [enum INRelativeReference](../Intents/inrelativereference.md)
  Constants indicating relative positions.
- [enum INRelativeSetting](../Intents/inrelativesetting.md)
  Constants indicating relative settings.
### CarPlay Resolution Results
- [class INCarSeatResolutionResult](../Intents/incarseatresolutionresult.md)
  A resolution result for a specific seat of the car.
- [class INCarDefrosterResolutionResult](../Intents/incardefrosterresolutionresult.md)
  A resolution result for which defroster to use in a car.
- [class INCarAudioSourceResolutionResult](../Intents/incaraudiosourceresolutionresult.md)
  A resolution result for the audio source to use in a car.
- [class INCarAirCirculationModeResolutionResult](../Intents/incaraircirculationmoderesolutionresult.md)
  A resolution result for the air circulation mode to use in a car.
- [class INRadioTypeResolutionResult](../Intents/inradiotyperesolutionresult.md)
  A resolution result for the type of radio to use in a car.
- [class INRelativeReferenceResolutionResult](../Intents/inrelativereferenceresolutionresult.md)
  A resolution result for a choice between the next or previous option.
- [class INRelativeSettingResolutionResult](../Intents/inrelativesettingresolutionresult.md)
  A resolution result for whether you can select the minimum, current, or maximum value.
### Money Transfers
- [protocol INTransferMoneyIntentHandling](../Intents/intransfermoneyintenthandling.md)
  The handler interface for transferring money between accounts.
- [class INTransferMoneyIntent](../Intents/intransfermoneyintent.md)
  A request to transfer money between two accounts.
- [class INTransferMoneyIntentResponse](../Intents/intransfermoneyintentresponse.md)
  Your app’s response to a request to transfer money.
### Note Additions
- [protocol INAppendToNoteIntentHandling](../Intents/inappendtonoteintenthandling.md)
  The handler interface for appending content to a note.
- [class INAppendToNoteIntent](../Intents/inappendtonoteintent.md)
  A request to append content to a note.
- [class INAppendToNoteIntentResponse](../Intents/inappendtonoteintentresponse.md)
  Your app’s response to a request to append content to a note.
### Photo Search
- [protocol INSearchForPhotosIntentHandling](../Intents/insearchforphotosintenthandling.md)
  The handler interface for searching the user’s photos.
- [class INSearchForPhotosIntent](../Intents/insearchforphotosintent.md)
  A request for the list of photos that match the specified criteria.
- [class INSearchForPhotosIntentResponse](../Intents/insearchforphotosintentresponse.md)
  Your app’s response to a search for photos intent.
### Photo Playback
- [protocol INStartPhotoPlaybackIntentHandling](../Intents/instartphotoplaybackintenthandling.md)
  The handler interface for searching the user’s photos and the playback of the results.
- [class INStartPhotoPlaybackIntent](../Intents/instartphotoplaybackintent.md)
  A request to search for photos and initiate a slideshow with the results.
- [class INStartPhotoPlaybackIntentResponse](../Intents/instartphotoplaybackintentresponse.md)
  Your app’s response to a start photo playback intent.
### Photo Data Objects
- [struct INPhotoAttributeOptions](../Intents/inphotoattributeoptions.md)
  Constants indicating attributes of a photo.
### Task Deletion
- [protocol INDeleteTasksIntentHandling](../Intents/indeletetasksintenthandling.md)
  An interface that handles requests to delete tasks from a task list.
- [class INDeleteTasksIntent](../Intents/indeletetasksintent.md)
  A request to delete one or more tasks.
- [class INDeleteTasksIntentResponse](../Intents/indeletetasksintentresponse.md)
  Your response to a request to delete tasks.
- [class INDeleteTasksTaskListResolutionResult](../Intents/indeletetaskstasklistresolutionresult.md)
  A resolution result for deleting task lists.
- [class INDeleteTasksTaskResolutionResult](../Intents/indeletetaskstaskresolutionresult.md)
  A resolution result for deleting tasks.
### Task List Creation
- [protocol INCreateTaskListIntentHandling](../Intents/increatetasklistintenthandling.md)
  The handler interface for creating task lists.
- [class INCreateTaskListIntent](../Intents/increatetasklistintent.md)
  A request to create a new task list.
- [class INCreateTaskListIntentResponse](../Intents/increatetasklistintentresponse.md)
  Your app’s response to a request to create a task list.
### Visual Codes
- [protocol INGetVisualCodeIntentHandling](../Intents/ingetvisualcodeintenthandling.md)
  The handler interface for displaying your app’s visual codes.
- [class INGetVisualCodeIntent](../Intents/ingetvisualcodeintent.md)
  A request for a visual code to use for exchanging payment and contact information.
- [class INGetVisualCodeIntentResponse](../Intents/ingetvisualcodeintentresponse.md)
  Your app’s response to a request for a visual code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/deprecated-symbols)*