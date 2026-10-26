# Restaurant Reservations

**Framework**: SiriKit  
**Role**: API Collection

Create and manage restaurant reservations with help from the Maps app.

#### Overview

Users can book restaurant reservations and view their current reservations from Maps. You provide Apple with information about the restaurants that you support before implementing support for these intents. When the user books a restaurant, Maps includes your information in the intents that it sends to your Intents app extension, which uses the information to complete the booking.

## Topics

### Book Restaurant Reservation
- [protocol INBookRestaurantReservationIntentHandling](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintenthandling)
  The handler interface booking a reservation that the user selected.
- [class INBookRestaurantReservationIntent](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintent)
  A request to create a reservation at the specified restaurant.
- [class INBookRestaurantReservationIntentResponse](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentresponse)
  Your app’s response to a book restaurant reservation intent.
### Get Available Restaurant Reservation Booking Defaults
- [protocol INGetAvailableRestaurantReservationBookingDefaultsIntentHandling](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintenthandling)
  The handler interface for providing default values to the system when pre-fetching an initial set of possible reservation times.
- [class INGetAvailableRestaurantReservationBookingDefaultsIntent](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintent)
  A request for the default values to use when fetching potential reservation options.
- [class INGetAvailableRestaurantReservationBookingDefaultsIntentResponse](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse)
  Your app’s response to a get available restaurant reservation booking defaults intent.
### Get Available Restaurant Reservation Bookings
- [protocol INGetAvailableRestaurantReservationBookingsIntentHandling](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintenthandling)
  The handler interface for generating a list of potential reservation times from which the user can select.
- [class INGetAvailableRestaurantReservationBookingsIntent](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintent)
  A request for the time slots available for making a reservation.
- [class INGetAvailableRestaurantReservationBookingsIntentResponse](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentresponse)
  Your app’s response to a get available restaurant reservation bookings intent.
### Get Restaurant Guest
- [protocol INGetRestaurantGuestIntentHandling](https://developer.apple.com/documentation/intents/ingetrestaurantguestintenthandling)
  The handler interface for fetching information about the person making a reservation.
- [class INGetRestaurantGuestIntent](https://developer.apple.com/documentation/intents/ingetrestaurantguestintent)
  A request for information about the guest who is making reservations.
- [class INGetRestaurantGuestIntentResponse](https://developer.apple.com/documentation/intents/ingetrestaurantguestintentresponse)
  Your app’s response to a get restaurant guest intent.
### Get User Current Restaurant Reservation Bookings
- [protocol INGetUserCurrentRestaurantReservationBookingsIntentHandling](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintenthandling)
  The handler interface for fetching and delivering the user’s current reservations.
- [class INGetUserCurrentRestaurantReservationBookingsIntent](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintent)
  A request for the list of the user’s current reservations.
- [class INGetUserCurrentRestaurantReservationBookingsIntentResponse](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintentresponse)
  Your app’s response to a get user current restaurant reservation bookings intent.
### Data Objects
- [class INRestaurant](https://developer.apple.com/documentation/intents/inrestaurant)
  A restaurant for which your app can make and manage reservations.
- [class INRestaurantGuest](https://developer.apple.com/documentation/intents/inrestaurantguest)
  The person assigned to a reservation.
- [class INRestaurantGuestDisplayPreferences](https://developer.apple.com/documentation/intents/inrestaurantguestdisplaypreferences)
  Options about how to display guest information from system interfaces.
- [class INRestaurantOffer](https://developer.apple.com/documentation/intents/inrestaurantoffer)
  Information about special offers made by a restaurant.
- [class INRestaurantReservationBooking](https://developer.apple.com/documentation/intents/inrestaurantreservationbooking)
  A potential reservation that a user can book.
- [class INRestaurantReservationUserBooking](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking)
  A reservation created by a user.
- [class INTermsAndConditions](https://developer.apple.com/documentation/intents/intermsandconditions)
  The terms and conditions of service when making restaurant reservations.
- [enum INRestaurantReservationUserBookingStatus](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbookingstatus)
  Constants indicating the status of a user reservation.
### Resolution Results
- [class INRestaurantResolutionResult](https://developer.apple.com/documentation/intents/inrestaurantresolutionresult)
  A resolution result for the restaurant selected by a user.
- [class INRestaurantGuestResolutionResult](https://developer.apple.com/documentation/intents/inrestaurantguestresolutionresult)
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