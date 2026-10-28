# Siri Event Suggestions

**Framework**: SiriKit  
**Role**: API Collection

Provide users with current, actionable information connected to a reservation.

## Overview

Siri can expose reservation information from your app in context and at specific times so the user can take relevant actions based on the circumstances. Your app donates an [`INInteraction`](../Intents/ininteraction.md) object that contains information about the reservation that can be sent to the user to allow them to confirm a hotel reservation, remind them to check in for a flight, help them return a rental car, and several other options.

> 💡 **Tip**:  If you send your users reservation information in email or web pages, use [Siri Event Suggestions Markup](../SiriEventSuggestionsMarkup/SiriEventSuggestionsMarkup.md) to provide the information to Siri as well. Siri uses reservation IDs to prevent duplicate entries.

Apps offering reservations with check-in capabilities can integrate with Shortcuts Suggestions on the Lock Screen and allow users to launch your app to complete checking in for their reservation. Create a new reservation object with an array of [`INReservationAction`](../Intents/inreservationaction.md) objects that contain a user activity and relevant time frame. Siri provides users with the ability to launch your app with the user activity and time frame information. For instance, a flight reservation app may provide users the ability to check-in for a flight starting 24 hours before the departure time.

## Topics

### Essentials
- [Donating Reservations](./donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Integrating Your App with Siri Event Suggestions](./integrating-your-app-with-siri-event-suggestions.md)
  Donate reservations and provide quick access to event details throughout the system.
### Reservation Details
- [class INGetReservationDetailsIntent](../Intents/ingetreservationdetailsintent.md)
  A request for details about one or more reservations.
- [class INGetReservationDetailsIntentResponse](../Intents/ingetreservationdetailsintentresponse.md)
  Your app’s response to a request for reservation details.
### Common Reservation Data Objects
- [class INReservation](../Intents/inreservation.md)
  An object that describes a reservation.
- [class INReservationAction](../Intents/inreservationaction.md)
  An action a user can perform that’s relevant to a reservation.
- [enum INReservationStatus](../Intents/inreservationstatus.md)
  Constants that describe the current status of the reservation.
- [class INSeat](../Intents/inseat.md)
  An object containing seat information associated with a reservation.
### Travel Reservations
- [class INFlightReservation](../Intents/inflightreservation.md)
  The information that describes a flight reservation.
- [class INTrainReservation](../Intents/intrainreservation.md)
  The information that describes a train reservation.
- [class INBoatReservation](../Intents/inboatreservation.md)
  The information that describes a boat reservation.
- [class INBusReservation](../Intents/inbusreservation.md)
  The information that describes a bus reservation.
- [class INRentalCarReservation](../Intents/inrentalcarreservation.md)
  The information that describes a rental car reservation.
### Food, Lodging, and Event Reservations
- [class INRestaurantReservation](../Intents/inrestaurantreservation.md)
  The information that describes a restaurant reservation.
- [class INLodgingReservation](../Intents/inlodgingreservation.md)
  The information that describes a lodging reservation.
- [class INTicketedEventReservation](../Intents/inticketedeventreservation.md)
  The information that describes a ticketed event reservation.

## See Also

### Shortcuts and Donations
- [Offering Actions in the Shortcuts App](./offering-actions-in-the-shortcuts-app.md)
  Suggest shortcuts users may want to add to Siri or combine with other actions in their own shortcuts.
- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](./adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Donating Shortcuts](./donating-shortcuts.md)
  Tell Siri about shortcuts to actions that the user performed in your app.
- [Deleting Donated Shortcuts](./deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Soup Chef: Accelerating App Interactions with Shortcuts](./soup-chef-accelerating-app-interactions-with-shortcuts.md)
  Make it easy for people to use Siri with your app by providing shortcuts to your app’s actions.
- [Soup Chef with App Intents: Migrating custom intents](./soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [Adding Shortcuts for Wind Down](./adding-shortcuts-for-wind-down.md)
  Reveal your app’s shortcuts inside the Health app.
- [class INShortcutReference](../Intents/inshortcutreference.md)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INInteraction](../Intents/ininteraction.md)
  An interaction between the user and your app involving an intent object.
- [enum INShortcut](../Intents/inshortcut-swift.enum.md)
  An action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INVoiceShortcutCenter](../Intents/invoiceshortcutcenter.md)
  Retrieve the user’s shortcuts and make shortcut suggestions.
- [class INVoiceShortcut](../Intents/invoiceshortcut.md)
  A shortcut the user added to Siri.
- [struct INShortcutAvailabilityOptions](../Intents/inshortcutavailabilityoptions.md)
  Defined contexts in which an intent or activity might be relevant to a user.
- [class INShortcutReference](../Intents/inshortcutreference.md)
  An object representing an action available in your app that the system may suggest to a user or a user may add to Siri.
- [class INIntentDonationMetadata](../Intents/inintentdonationmetadata.md)
- [Apple Watch support](./watch-and-widget-support.md)
  Display relevant shortcuts on the Siri watch face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/siri-event-suggestions)*