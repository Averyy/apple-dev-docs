# Restaurant Reservations

**Framework**: SiriKit  
**Role**: API Collection

Create and manage restaurant reservations with help from the Maps app.

#### Overview

Users can book restaurant reservations and view their current reservations from Maps. You provide Apple with information about the restaurants that you support before implementing support for these intents. When the user books a restaurant, Maps includes your information in the intents that it sends to your Intents app extension, which uses the information to complete the booking.

## Topics

### Book Restaurant Reservation
- [protocol INBookRestaurantReservationIntentHandling](../Intents/inbookrestaurantreservationintenthandling.md)
  The handler interface booking a reservation that the user selected.
- [class INBookRestaurantReservationIntent](../Intents/inbookrestaurantreservationintent.md)
  A request to create a reservation at the specified restaurant.
- [class INBookRestaurantReservationIntentResponse](../Intents/inbookrestaurantreservationintentresponse.md)
  Your app’s response to a book restaurant reservation intent.
### Get Available Restaurant Reservation Booking Defaults
- [protocol INGetAvailableRestaurantReservationBookingDefaultsIntentHandling](../Intents/ingetavailablerestaurantreservationbookingdefaultsintenthandling.md)
  The handler interface for providing default values to the system when pre-fetching an initial set of possible reservation times.
- [class INGetAvailableRestaurantReservationBookingDefaultsIntent](../Intents/ingetavailablerestaurantreservationbookingdefaultsintent.md)
  A request for the default values to use when fetching potential reservation options.
- [class INGetAvailableRestaurantReservationBookingDefaultsIntentResponse](../Intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse.md)
  Your app’s response to a get available restaurant reservation booking defaults intent.
### Get Available Restaurant Reservation Bookings
- [protocol INGetAvailableRestaurantReservationBookingsIntentHandling](../Intents/ingetavailablerestaurantreservationbookingsintenthandling.md)
  The handler interface for generating a list of potential reservation times from which the user can select.
- [class INGetAvailableRestaurantReservationBookingsIntent](../Intents/ingetavailablerestaurantreservationbookingsintent.md)
  A request for the time slots available for making a reservation.
- [class INGetAvailableRestaurantReservationBookingsIntentResponse](../Intents/ingetavailablerestaurantreservationbookingsintentresponse.md)
  Your app’s response to a get available restaurant reservation bookings intent.
### Get Restaurant Guest
- [protocol INGetRestaurantGuestIntentHandling](../Intents/ingetrestaurantguestintenthandling.md)
  The handler interface for fetching information about the person making a reservation.
- [class INGetRestaurantGuestIntent](../Intents/ingetrestaurantguestintent.md)
  A request for information about the guest who is making reservations.
- [class INGetRestaurantGuestIntentResponse](../Intents/ingetrestaurantguestintentresponse.md)
  Your app’s response to a get restaurant guest intent.
### Get User Current Restaurant Reservation Bookings
- [protocol INGetUserCurrentRestaurantReservationBookingsIntentHandling](../Intents/ingetusercurrentrestaurantreservationbookingsintenthandling.md)
  The handler interface for fetching and delivering the user’s current reservations.
- [class INGetUserCurrentRestaurantReservationBookingsIntent](../Intents/ingetusercurrentrestaurantreservationbookingsintent.md)
  A request for the list of the user’s current reservations.
- [class INGetUserCurrentRestaurantReservationBookingsIntentResponse](../Intents/ingetusercurrentrestaurantreservationbookingsintentresponse.md)
  Your app’s response to a get user current restaurant reservation bookings intent.
### Data Objects
- [class INRestaurant](../Intents/inrestaurant.md)
  A restaurant for which your app can make and manage reservations.
- [class INRestaurantGuest](../Intents/inrestaurantguest.md)
  The person assigned to a reservation.
- [class INRestaurantGuestDisplayPreferences](../Intents/inrestaurantguestdisplaypreferences.md)
  Options about how to display guest information from system interfaces.
- [class INRestaurantOffer](../Intents/inrestaurantoffer.md)
  Information about special offers made by a restaurant.
- [class INRestaurantReservationBooking](../Intents/inrestaurantreservationbooking.md)
  A potential reservation that a user can book.
- [class INRestaurantReservationUserBooking](../Intents/inrestaurantreservationuserbooking.md)
  A reservation created by a user.
- [class INTermsAndConditions](../Intents/intermsandconditions.md)
  The terms and conditions of service when making restaurant reservations.
- [enum INRestaurantReservationUserBookingStatus](../Intents/inrestaurantreservationuserbookingstatus.md)
  Constants indicating the status of a user reservation.
### Resolution Results
- [class INRestaurantResolutionResult](../Intents/inrestaurantresolutionresult.md)
  A resolution result for the restaurant selected by a user.
- [class INRestaurantGuestResolutionResult](../Intents/inrestaurantguestresolutionresult.md)
  A resolution result for the identity of a user involved in booking a reservation at a restaurant.

## See Also

### Standard Intents
- [Car Commands](./car-commands.md)
  Manage vehicle door locks and get the vehicle’s status.
- [Lists and Notes](./lists-and-notes.md)
  Create and manage notes and to-do list items.
- [Media](./media.md)
  Listen and control audio through Siri Intents, or listen and watch media content from your app with shortcuts.
- [Messaging](./messaging.md)
  Send messages and search the user’s received messages.
- [Payments](./payments.md)
  Send payments between users or pay bills.
- [Ride Booking](./ride-booking.md)
  Book rides and report their status.
- [VoIP Calling](./voip-calling.md)
  Initiate calls and search the user’s call history.
- [Workouts](./workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/restaurant-reservations)*