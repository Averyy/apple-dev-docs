# Deprecated Symbols

**Framework**: SiriKit  
**Role**: API Collection

Review unsupported symbols and their replacements.

#### Overview

Many deprecated system intents have no replacement. You may continue to provide these features by defining custom intents. For more information about custom intents, see [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](./adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md).

## Topics

### Audio Call Initiation
- [protocol INStartAudioCallIntentHandling](https://developer.apple.com/documentation/intents/instartaudiocallintenthandling)
  The handler interface for initiating an audio call from your app.
- [class INStartAudioCallIntent](https://developer.apple.com/documentation/intents/instartaudiocallintent)
  A request to start an audio-only call with one or more users.
- [class INStartAudioCallIntentResponse](https://developer.apple.com/documentation/intents/instartaudiocallintentresponse)
  An app’s response to an intent to start an audio call.
### Video Call Initiation
- [protocol INStartVideoCallIntentHandling](https://developer.apple.com/documentation/intents/instartvideocallintenthandling)
  The handler interface for initiating a video call from your app.
- [class INStartVideoCallIntent](https://developer.apple.com/documentation/intents/instartvideocallintent)
  A request to start a video call with one or more users.
- [class INStartVideoCallIntentResponse](https://developer.apple.com/documentation/intents/instartvideocallintentresponse)
  A response to an intent to start a video call.
### Note Content
- [enum INNoteContentType](https://developer.apple.com/documentation/intents/innotecontenttype)
  Constants indicating the type of content represented by the note.
- [class INNoteContentTypeResolutionResult](https://developer.apple.com/documentation/intents/innotecontenttyperesolutionresult)
  A resolution result for the type of data contained in notes.
### Domain-Handling Protocols
- [protocol INMessagesDomainHandling](https://developer.apple.com/documentation/intents/inmessagesdomainhandling)
  An interface for adopting all of the protocols in the messages domain.
- [protocol INNotebookDomainHandling](https://developer.apple.com/documentation/intents/innotebookdomainhandling)
  An interface for adopting all of the protocols in the lists and notes domain.
- [protocol INWorkoutsDomainHandling](https://developer.apple.com/documentation/intents/inworkoutsdomainhandling)
  An interface for adopting all of the protocols in the workouts domain.
- [protocol INPaymentsDomainHandling](https://developer.apple.com/documentation/intents/inpaymentsdomainhandling)
  An interface for adopting all of the protocols in the payments domain.
- [protocol INCallsDomainHandling](https://developer.apple.com/documentation/intents/incallsdomainhandling)
  Provides a convenient way to adopt all of the protocols in the VoIP calling domain.
- [protocol INVisualCodeDomainHandling](https://developer.apple.com/documentation/intents/invisualcodedomainhandling)
  An interface for adopting all of the protocols in the visual codes domain.
- [protocol INPhotosDomainHandling](https://developer.apple.com/documentation/intents/inphotosdomainhandling)
  An interface for adopting all of the protocols in the photos domain.
- [protocol INRidesharingDomainHandling](https://developer.apple.com/documentation/intents/inridesharingdomainhandling)
  An interface for adopting all of the protocols in the ride-booking domain.
- [protocol INCarCommandsDomainHandling](https://developer.apple.com/documentation/intents/incarcommandsdomainhandling)
  An interface for adopting all the handling protocols in the car commands domain.
- [protocol INCarPlayDomainHandling](https://developer.apple.com/documentation/intents/incarplaydomainhandling)
  An interface for adopting all of the protocols in the CarPlay domain.
- [protocol INRadioDomainHandling](https://developer.apple.com/documentation/intents/inradiodomainhandling)
  An interface for adopting all of the protocols in the radio domain.
### Bill Payment
- [protocol INPayBillIntentHandling](https://developer.apple.com/documentation/intents/inpaybillintenthandling)
  The handler interface for paying a bill using money from the user’s account.
- [class INPayBillIntent](https://developer.apple.com/documentation/intents/inpaybillintent)
  A request to transfer money to facilitate payment of a bill.
- [class INPayBillIntentResponse](https://developer.apple.com/documentation/intents/inpaybillintentresponse)
  Your app’s response to a request to pay a bill.
### Bill Search
- [protocol INSearchForBillsIntentHandling](https://developer.apple.com/documentation/intents/insearchforbillsintenthandling)
  The handler interface for searching for bills associated with the user.
- [class INSearchForBillsIntent](https://developer.apple.com/documentation/intents/insearchforbillsintent)
  A request for the list of bills matching the specified criteria.
- [class INSearchForBillsIntentResponse](https://developer.apple.com/documentation/intents/insearchforbillsintentresponse)
  Your app’s response to a request to a search for bills.
### Bill Data Objects
- [class INBillDetails](https://developer.apple.com/documentation/intents/inbilldetails)
  The detailed information associated with a bill.
- [class INBillPayee](https://developer.apple.com/documentation/intents/inbillpayee)
  The entity that receives the proceeds from a bill payment.
- [class INBillTypeResolutionResult](https://developer.apple.com/documentation/intents/inbilltyperesolutionresult)
  A resolution result for the types of bills a user might pay.
- [class INBillPayeeResolutionResult](https://developer.apple.com/documentation/intents/inbillpayeeresolutionresult)
  A resolution result for the recipient of a bill payment.
- [class INVisualCodeTypeResolutionResult](https://developer.apple.com/documentation/intents/invisualcodetyperesolutionresult)
  A resolution result for the type of visual code used to exchange information.
### Call History Search
- [protocol INSearchCallHistoryIntentHandling](https://developer.apple.com/documentation/intents/insearchcallhistoryintenthandling)
  The handler interface for searching the user’s call history.
- [class INSearchCallHistoryIntent](https://developer.apple.com/documentation/intents/insearchcallhistoryintent)
  A request to list the calls matching the specified criteria.
- [class INSearchCallHistoryIntentResponse](https://developer.apple.com/documentation/intents/insearchcallhistoryintentresponse)
  Your app’s response to a search call history intent.
### CarPlay Audio Source
- [protocol INSetAudioSourceInCarIntentHandling](https://developer.apple.com/documentation/intents/insetaudiosourceincarintenthandling)
  The handler interface for changing a vehicle’s audio source.
- [class INSetAudioSourceInCarIntent](https://developer.apple.com/documentation/intents/insetaudiosourceincarintent)
  A request to change the source of audio playback in a CarPlay-enabled vehicle.
- [class INSetAudioSourceInCarIntentResponse](https://developer.apple.com/documentation/intents/insetaudiosourceincarintentresponse)
  Your app’s response to a set audio source in car intent.
### CarPlay Climate Settings
- [protocol INSetClimateSettingsInCarIntentHandling](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintenthandling)
  The handler interface for changing a vehicle’s climate control settings.
- [class INSetClimateSettingsInCarIntent](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent)
  A request to change the climate settings in a CarPlay-enabled vehicle.
- [class INSetClimateSettingsInCarIntentResponse](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintentresponse)
  Your app’s response to a set climate settings in car intent.
### CarPlay Defroster Settings
- [protocol INSetDefrosterSettingsInCarIntentHandling](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintenthandling)
  The handler interface for changing a vehicle’s defroster settings.
- [class INSetDefrosterSettingsInCarIntent](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintent)
  A request to change the defroster settings in a CarPlay-enabled vehicle.
- [class INSetDefrosterSettingsInCarIntentResponse](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintentresponse)
  Your app’s response to a set defroster settings in car intent.
### CarPlay Profile Saving
- [protocol INSaveProfileInCarIntentHandling](https://developer.apple.com/documentation/intents/insaveprofileincarintenthandling)
  The handler interface for saving vehicle environment settings to a user-specified profile.
- [class INSaveProfileInCarIntent](https://developer.apple.com/documentation/intents/insaveprofileincarintent)
  A request to save the user’s vehicle environment settings in a CarPlay-enabled vehicle.
- [class INSaveProfileInCarIntentResponse](https://developer.apple.com/documentation/intents/insaveprofileincarintentresponse)
  Your app’s response to a save profile in car intent.
### CarPlay Profile Settings
- [protocol INSetProfileInCarIntentHandling](https://developer.apple.com/documentation/intents/insetprofileincarintenthandling)
  The handler interface for restoring vehicle environment settings from a user-specified profile.
- [class INSetProfileInCarIntent](https://developer.apple.com/documentation/intents/insetprofileincarintent)
  A request to change the user’s vehicle environment settings to the ones from the specified profile.
- [class INSetProfileInCarIntentResponse](https://developer.apple.com/documentation/intents/insetprofileincarintentresponse)
  Your app’s response to a set profile in car intent.
### CarPlay Radio Station Settings
- [protocol INSetRadioStationIntentHandling](https://developer.apple.com/documentation/intents/insetradiostationintenthandling)
  The handler interface for changing a radio station.
- [class INSetRadioStationIntent](https://developer.apple.com/documentation/intents/insetradiostationintent)
  A request to change the current radio station.
- [class INSetRadioStationIntentResponse](https://developer.apple.com/documentation/intents/insetradiostationintentresponse)
  Your app’s response to a set radio station intent.
### CarPlay Seat Settings
- [protocol INSetSeatSettingsInCarIntentHandling](https://developer.apple.com/documentation/intents/insetseatsettingsincarintenthandling)
  The handler interface for changing a vehicle’s seat-related settings.
- [class INSetSeatSettingsInCarIntent](https://developer.apple.com/documentation/intents/insetseatsettingsincarintent)
  A request to change the seat-related settings in a CarPlay-enabled vehicle.
- [class INSetSeatSettingsInCarIntentResponse](https://developer.apple.com/documentation/intents/insetseatsettingsincarintentresponse)
  Your app’s response to a set seat settings in car intent.
### CarPlay Data Objects
- [enum INCarSeat](https://developer.apple.com/documentation/intents/incarseat)
  Constants indicating a seat position.
- [enum INCarDefroster](https://developer.apple.com/documentation/intents/incardefroster)
  Constants indicating the defroster type.
- [enum INCarAudioSource](https://developer.apple.com/documentation/intents/incaraudiosource)
  Constants indicating the source of audio.
- [enum INCarAirCirculationMode](https://developer.apple.com/documentation/intents/incaraircirculationmode)
  Constants indicating the circulation mode for the climate system.
- [enum INRadioType](https://developer.apple.com/documentation/intents/inradiotype)
  Constants indicating the type of radio.
- [enum INRelativeReference](https://developer.apple.com/documentation/intents/inrelativereference)
  Constants indicating relative positions.
- [enum INRelativeSetting](https://developer.apple.com/documentation/intents/inrelativesetting)
  Constants indicating relative settings.
### CarPlay Resolution Results
- [class INCarSeatResolutionResult](https://developer.apple.com/documentation/intents/incarseatresolutionresult)
  A resolution result for a specific seat of the car.
- [class INCarDefrosterResolutionResult](https://developer.apple.com/documentation/intents/incardefrosterresolutionresult)
  A resolution result for which defroster to use in a car.
- [class INCarAudioSourceResolutionResult](https://developer.apple.com/documentation/intents/incaraudiosourceresolutionresult)
  A resolution result for the audio source to use in a car.
- [class INCarAirCirculationModeResolutionResult](https://developer.apple.com/documentation/intents/incaraircirculationmoderesolutionresult)
  A resolution result for the air circulation mode to use in a car.
- [class INRadioTypeResolutionResult](https://developer.apple.com/documentation/intents/inradiotyperesolutionresult)
  A resolution result for the type of radio to use in a car.
- [class INRelativeReferenceResolutionResult](https://developer.apple.com/documentation/intents/inrelativereferenceresolutionresult)
  A resolution result for a choice between the next or previous option.
- [class INRelativeSettingResolutionResult](https://developer.apple.com/documentation/intents/inrelativesettingresolutionresult)
  A resolution result for whether you can select the minimum, current, or maximum value.
### Money Transfers
- [protocol INTransferMoneyIntentHandling](https://developer.apple.com/documentation/intents/intransfermoneyintenthandling)
  The handler interface for transferring money between accounts.
- [class INTransferMoneyIntent](https://developer.apple.com/documentation/intents/intransfermoneyintent)
  A request to transfer money between two accounts.
- [class INTransferMoneyIntentResponse](https://developer.apple.com/documentation/intents/intransfermoneyintentresponse)
  Your app’s response to a request to transfer money.
### Note Additions
- [protocol INAppendToNoteIntentHandling](https://developer.apple.com/documentation/intents/inappendtonoteintenthandling)
  The handler interface for appending content to a note.
- [class INAppendToNoteIntent](https://developer.apple.com/documentation/intents/inappendtonoteintent)
  A request to append content to a note.
- [class INAppendToNoteIntentResponse](https://developer.apple.com/documentation/intents/inappendtonoteintentresponse)
  Your app’s response to a request to append content to a note.
### Photo Search
- [protocol INSearchForPhotosIntentHandling](https://developer.apple.com/documentation/intents/insearchforphotosintenthandling)
  The handler interface for searching the user’s photos.
- [class INSearchForPhotosIntent](https://developer.apple.com/documentation/intents/insearchforphotosintent)
  A request for the list of photos that match the specified criteria.
- [class INSearchForPhotosIntentResponse](https://developer.apple.com/documentation/intents/insearchforphotosintentresponse)
  Your app’s response to a search for photos intent.
### Photo Playback
- [protocol INStartPhotoPlaybackIntentHandling](https://developer.apple.com/documentation/intents/instartphotoplaybackintenthandling)
  The handler interface for searching the user’s photos and the playback of the results.
- [class INStartPhotoPlaybackIntent](https://developer.apple.com/documentation/intents/instartphotoplaybackintent)
  A request to search for photos and initiate a slideshow with the results.
- [class INStartPhotoPlaybackIntentResponse](https://developer.apple.com/documentation/intents/instartphotoplaybackintentresponse)
  Your app’s response to a start photo playback intent.
### Photo Data Objects
- [struct INPhotoAttributeOptions](https://developer.apple.com/documentation/intents/inphotoattributeoptions)
  Constants indicating attributes of a photo.
### Task Deletion
- [protocol INDeleteTasksIntentHandling](https://developer.apple.com/documentation/intents/indeletetasksintenthandling)
  An interface that handles requests to delete tasks from a task list.
- [class INDeleteTasksIntent](https://developer.apple.com/documentation/intents/indeletetasksintent)
  A request to delete one or more tasks.
- [class INDeleteTasksIntentResponse](https://developer.apple.com/documentation/intents/indeletetasksintentresponse)
  Your response to a request to delete tasks.
- [class INDeleteTasksTaskListResolutionResult](https://developer.apple.com/documentation/intents/indeletetaskstasklistresolutionresult)
  A resolution result for deleting task lists.
- [class INDeleteTasksTaskResolutionResult](https://developer.apple.com/documentation/intents/indeletetaskstaskresolutionresult)
  A resolution result for deleting tasks.
### Task List Creation
- [protocol INCreateTaskListIntentHandling](https://developer.apple.com/documentation/intents/increatetasklistintenthandling)
  The handler interface for creating task lists.
- [class INCreateTaskListIntent](https://developer.apple.com/documentation/intents/increatetasklistintent)
  A request to create a new task list.
- [class INCreateTaskListIntentResponse](https://developer.apple.com/documentation/intents/increatetasklistintentresponse)
  Your app’s response to a request to create a task list.
### Visual Codes
- [protocol INGetVisualCodeIntentHandling](https://developer.apple.com/documentation/intents/ingetvisualcodeintenthandling)
  The handler interface for displaying your app’s visual codes.
- [class INGetVisualCodeIntent](https://developer.apple.com/documentation/intents/ingetvisualcodeintent)
  A request for a visual code to use for exchanging payment and contact information.
- [class INGetVisualCodeIntentResponse](https://developer.apple.com/documentation/intents/ingetvisualcodeintentresponse)
  Your app’s response to a request for a visual code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/deprecated-symbols)*